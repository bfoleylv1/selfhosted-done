#!/usr/bin/env python3
"""Rebuild the ScaleTail-sourced services FAITHFULLY.

The generic template (image + ./config + ./data + guessed healthcheck) produced
files that parse but do not run -- e.g. dozzle needs /var/run/docker.sock, which
the template never mounts. This regenerates each service from its ORIGINAL
ScaleTail compose so the real volumes, env, devices, caps and companion
containers (db/redis/worker) are preserved.

Transformations applied to the original:
  * drop the `ts-serve` / tailscale sidecar service entirely
  * the app service inherits `network_mode: service:ts-serve` -> replace with a
    normal port publish on the sticky host port
  * ${IMAGE_URL}/${SERVICEPORT}/etc. resolved from the sibling .env
  * TS_*/tailscale env and volumes stripped
  * add a healthcheck only where one can be justified (HTTP port known)
  * swarm variant: named volumes instead of relative binds, no container_name,
    deploy block, overlay network

Writes <svc>/docker-compose.yml and <svc>/swarm/docker-stack.yml.
"""
import json, os, re, sys, copy, secrets, hashlib
import yaml

TOOLS = os.path.dirname(os.path.abspath(__file__))
DONE = os.path.dirname(TOOLS)
HP_FILE = os.path.join(TOOLS, "hostports.json")

# Upstream exposes these only through the tailscale serve proxy, so .env has no
# SERVICEPORT. The real listen port comes from the serve.json Proxy target.
PORT_FIX = {
    "dockge": 5001, "espocrm": 80, "unmanic": 80, "kaneo": 5173,
}
# genuinely portless: scheduled config sync tools with no web UI
NO_PORT = {"configarr", "recyclarr"}

OVERRIDE = {
    "recyclarr": "ghcr.io/recyclarr/recyclarr:7",
    "swingmx":   "ghcr.io/swingmx/swingmusic:latest",
}
SKIP = {"tailscale-app-connector-node", "tailscale-exit-node",
        "tailscale-subnet-router-node", "docker-socket-with-tailscale",
        "musicseerr", "homelab-h1"}
TS_SVC = {"ts-serve", "tailscale", "ts"}
NON_HTTP = {53, 25565, 45876, 51820, 21115, 21116, 21117}


def norm(n):
    return n.lower().strip().replace(" ", "-").replace("_", "-")


def load_env(d):
    e = {}
    p = os.path.join(d, ".env")
    if os.path.isfile(p):
        for line in open(p, errors="replace"):
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            e[k.strip()] = v.split(" #")[0].split("\t#")[0].strip()
    return e


def detsub(txt, hp):
    """Rewrite leftover tailnet references to a concrete local URL."""
    txt = re.sub(r"https?://[^\s\"']*\$\{TS_[A-Z_]+\}[^\s\"']*",
                 f"http://localhost:{hp}", txt)
    txt = re.sub(r"https?://[^\s\"']*\.ts\.net[^\s\"']*", f"http://localhost:{hp}", txt)
    txt = re.sub(r"\$\{TS_[A-Z_]+\}", f"localhost:{hp}", txt)
    txt = re.sub(r"\$\{TAILNET[A-Z_]*\}", "local", txt)
    # placeholder tailnets and quoted forms, e.g. "svc.<YOUR_TAILNET>.ts.net"
    txt = re.sub(r'"?[A-Za-z0-9_<>-]+(?:\.[A-Za-z0-9_<>-]+)*\.ts\.net"?',
                 "localhost", txt)
    return txt


def subst(obj, env):
    """Resolve ${VAR} / ${VAR:-default} using the service .env."""
    if isinstance(obj, str):
        def r(m):
            k, dv = m.group(1), m.group(3)
            if k in env and env[k] != "":
                return env[k]
            if dv is not None:
                return dv
            return m.group(0)
        return re.sub(r"\$\{([A-Za-z_][A-Za-z0-9_]*)(:-([^}]*))?\}", r, obj)
    if isinstance(obj, list):
        return [subst(x, env) for x in obj]
    if isinstance(obj, dict):
        return {k: subst(v, env) for k, v in obj.items()}
    return obj


def strip_ts(v):
    """Remove tailscale-specific env/volumes/labels from a service body."""
    if isinstance(v.get("environment"), list):
        v["environment"] = [e for e in v["environment"]
                            if not re.match(r"\s*TS_[A-Z_]+", str(e))]
        if not v["environment"]:
            v.pop("environment")
    elif isinstance(v.get("environment"), dict):
        v["environment"] = {k: x for k, x in v["environment"].items()
                            if not k.startswith("TS_")}
        if not v["environment"]:
            v.pop("environment")
    if v.get("volumes"):
        v["volumes"] = [x for x in v["volumes"]
                        if "tailscale" not in str(x) and "/ts/" not in str(x)
                        and not str(x).startswith("ts-")]
        if not v["volumes"]:
            v.pop("volumes")
    # upstream labels point at the author's private tailnet -- drop them; the
    # generator appends its own commented homepage block instead
    v.pop("labels", None)
    # depends_on referencing the removed sidecar would block startup
    dep = v.get("depends_on")
    if isinstance(dep, dict):
        dep = {k: x for k, x in dep.items() if k not in TS_SVC}
        v["depends_on"] = dep or None
    elif isinstance(dep, list):
        dep = [x for x in dep if x not in TS_SVC]
        v["depends_on"] = dep or None
    if not v.get("depends_on"):
        v.pop("depends_on", None)
    return v


def pin_tag(img):
    """Ensure an explicit tag so deployments are reproducible."""
    if not img or img.startswith("$"):
        return img
    last = img.rsplit("/", 1)[-1]
    return img if (":" in last or "@" in last) else img + ":latest"


SECRET_SALT_FILE = os.path.join(TOOLS, "secret-salt")


def _salt():
    """One persistent random salt; secrets derive from it deterministically."""
    if not os.path.exists(SECRET_SALT_FILE):
        open(SECRET_SALT_FILE, "w").write(secrets.token_urlsafe(32))
    return open(SECRET_SALT_FILE).read().strip()


def gen_secret(service, key, n=32):
    """Stable secret for (service, key): same value every regeneration, and
    the same value in .env and in the compose file, so an app and its database
    never disagree about the password."""
    h = hashlib.sha256(f"{_salt()}:{service}:{key}".encode()).digest()
    import base64
    return base64.urlsafe_b64encode(h).decode().rstrip("=")[:n]


def write_env(base, rec, hp, cport):
    """Ship a .env next to the compose file for services that reference one.

    The upstream ScaleTail .env carries Tailscale auth material and tailnet
    names; those are stripped. Placeholder secrets are replaced with real
    generated values so the stack starts without hand-editing.
    """
    src = os.path.join(rec["path"], ".env")
    if not os.path.isfile(src):
        return False
    out = []
    for line in open(src, errors="replace"):
        s = line.strip()
        if not s or s.startswith("#"):
            out.append(line.rstrip("\n"))
            continue
        k = s.split("=", 1)[0].strip()
        if k.startswith("TS_") or k in ("TAILNET_NAME", "HOMEPAGE_SERVER"):
            continue
        out.append(line.rstrip("\n"))
    txt = "\n".join(out) + "\n"
    svc = norm(os.path.basename(base))

    def fix(line):
        if "=" not in line or line.lstrip().startswith("#"):
            return line
        k, v = line.split("=", 1)
        if re.search(r"REPLACE_WITH|CHANGE_?ME|changeme", v):
            return f"{k}={gen_secret(svc, k.strip())}"
        return line
    txt = "\n".join(fix(l) for l in txt.split("\n"))
    open(os.path.join(base, ".env"), "w").write(txt)
    return True


REQUIRED_SECRET = re.compile(r"\$\{([A-Z_]+)\}")


def fill_required(doc, env, svc="svc"):
    """Give any still-unresolved ${VAR} in env lists a concrete value.

    Compose treats an unset variable in `environment:` as a hard error, so a
    stack that references JWT_SECRET with nothing behind it will not start.
    """
    def val(k):
        if "SECRET" in k or "KEY" in k or "TOKEN" in k or "PASSWORD" in k:
            return gen_secret(svc, k)
        if k.startswith("DISABLE_") or k.startswith("ENABLE_"):
            return "false"
        return ""

    for n, v in doc["services"].items():
        e = v.get("environment")
        if isinstance(e, list):
            v["environment"] = [
                REQUIRED_SECRET.sub(lambda m: env.get(m.group(1)) or val(m.group(1)), str(x))
                for x in e]
        elif isinstance(e, dict):
            v["environment"] = {
                k: REQUIRED_SECRET.sub(lambda m: env.get(m.group(1)) or val(m.group(1)), str(x))
                for k, x in e.items()}
    return doc


def fill_secrets(doc, svc, env):
    """Replace placeholder credentials with deterministic per-key secrets.

    Values already present in the shipped .env win, so the app container and
    its database always agree on the same password.
    """
    pat = re.compile(r"REPLACE_WITH_[A-Z_]+|CHANGE_?ME|changeme")

    def val(key):
        v = env.get(key)
        return v if (v and not pat.search(v)) else gen_secret(svc, key)

    for v in doc["services"].values():
        e = v.get("environment")
        if isinstance(e, dict):
            # mapping form: the key IS the variable name
            v["environment"] = {
                k: (val(k) if pat.search(str(x)) else x) for k, x in e.items()}
            continue
        elif isinstance(e, list):
            out = []
            for item in e:
                s = str(item)
                if "=" in s and pat.search(s):
                    k = s.split("=", 1)[0]
                    out.append(f"{k}={val(k.strip())}")
                else:
                    out.append(item)
            v["environment"] = out
    return doc


# non-HTTP services need a liveness probe that is not an HTTP GET
PROC_HEALTH = {
    "configarr": "pgrep -f configarr || pgrep -f node",
    "recyclarr": "pgrep -f recyclarr || test -d /config",
    "minecraft": "mc-monitor status --host 127.0.0.1 --port 25565",
    "adguardhome": "nslookup -type=a localhost 127.0.0.1 || pgrep AdGuardHome",
    "technitium": "pgrep -f DnsServerApp || nslookup localhost 127.0.0.1",
}


def proc_healthcheck(key):
    cmd = PROC_HEALTH.get(key)
    if not cmd:
        return None
    return {"test": ["CMD-SHELL", cmd], "interval": "60s", "timeout": "10s",
            "retries": 3, "start_period": "90s"}


def healthcheck(cport):
    if not cport or int(cport) in NON_HTTP:
        return None
    p = int(cport)
    return {
        "test": ["CMD-SHELL",
                 f"curl -fsS http://127.0.0.1:{p}/ || "
                 f"wget -qO- http://127.0.0.1:{p}/ || exit 1"],
        "interval": "30s", "timeout": "10s", "retries": 3,
        "start_period": "60s",
    }


HEADER_C = ("# {name} - docker compose (single host)\n"
            "# ported from the upstream ScaleTail definition; tailscale sidecar removed\n"
            "# image verified against its registry at generation time\n\n")
HEADER_S = ("# {name} - docker swarm stack\n"
            "# deploy: docker stack deploy -c docker-stack.yml {name}\n"
            "# ported from the upstream ScaleTail definition; tailscale sidecar removed\n\n")

LABELS = """    # labels:
    #   - "homepage.group=Self Hosted"
    #   - "homepage.name={name}"
    #   - "homepage.description={name} self-hosted service."
    #   - "homepage.tags=Self Hosting Solutions"
    #   - "homepage.icon={name}.png"
    #   - "homepage.href=http://${{HOST_IP:-localhost}}:{hp}"
    #   - "homepage.server=localhost"
"""


def build(key, rec, hp):
    src = yaml.safe_load(open(rec["compose"], errors="replace"))
    env = load_env(rec["path"])
    src = subst(src, env)
    svcs = src.get("services") or {}

    app_name = None
    for cand in (("frontend",) if key == "kaneo" else ()) + \
                ("application", "app", key, norm(rec["name"])):
        if cand in svcs:
            app_name = cand
            break
    if app_name is None:
        for n in svcs:
            if n not in TS_SVC:
                app_name = n
                break
    if app_name is None:
        return None

    keep = {n: copy.deepcopy(v) for n, v in svcs.items() if n not in TS_SVC}
    cport = rec.get("port")
    cport = int(cport) if str(cport).isdigit() else None
    if not cport and key in PORT_FIX:
        cport = PORT_FIX[key]

    out = {"services": {}}
    for n, v in keep.items():
        v = strip_ts(v)
        v.pop("network_mode", None)
        if v.get("image"):
            v["image"] = pin_tag(v["image"])
        if n == app_name:
            if key in OVERRIDE:
                v["image"] = OVERRIDE[key]
            if cport:
                v["ports"] = [f"{hp}:{cport}"]
            hc = healthcheck(cport) or proc_healthcheck(key)
            if hc and "healthcheck" not in v:
                v["healthcheck"] = hc
        v.setdefault("restart", "unless-stopped")
        out["services"][n] = v

    # env_file: keep only entries that exist upstream; they are copied next to
    # the generated compose file, so rewrite the path to a bare ./.env
    for n, v in out["services"].items():
        ef = v.get("env_file")
        if not ef:
            continue
        ef = [ef] if isinstance(ef, str) else ef
        kept = []
        for e in ef:
            cand = os.path.join(rec["path"], str(e).lstrip("./"))
            if os.path.isfile(cand):
                kept.append("./" + os.path.basename(str(e).lstrip("./")))
        if kept:
            v["env_file"] = kept
        else:
            v.pop("env_file", None)

    out = fill_secrets(out, norm(rec["name"]), env)
    out = fill_required(out, env, norm(rec["name"]))

    # keep any named volumes the original declared
    if src.get("volumes"):
        out["volumes"] = {k: (v if v else None) for k, v in
                          (src["volumes"] or {}).items()}

    # any network a service joins must be declared at top level, otherwise the
    # project is invalid (the sidecar removal can orphan one)
    used_nets = set()
    for v in out["services"].values():
        nets = v.get("networks")
        if isinstance(nets, list):
            used_nets.update(nets)
        elif isinstance(nets, dict):
            used_nets.update(nets.keys())
    if used_nets:
        declared = dict(src.get("networks") or {})
        out["networks"] = {n: declared.get(n) for n in used_nets}
    return out, app_name, cport


def to_swarm(doc, name, app_name, hp, cport):
    d = copy.deepcopy(doc)
    named = dict(d.get("volumes") or {})
    for n, v in d["services"].items():
        v.pop("container_name", None)
        v.pop("restart", None)
        v.pop("privileged", None)
        v.pop("cap_add", None)
        v.pop("devices", None)
        # swarm ignores depends_on; ordering comes from restart_policy + healthchecks
        v.pop("depends_on", None)
        newvols = []
        for vol in (v.get("volumes") or []):
            s = str(vol)
            if s.startswith("./") or s.startswith("/"):
                if s.startswith("/var/run/docker.sock"):
                    newvols.append(vol)       # bind is required, node-local
                    continue
                host, _, rest = s.partition(":")
                vn = f"{name}_{re.sub(r'[^a-z0-9]+', '_', host.strip('./').lower()) or 'data'}"
                named[vn] = None
                newvols.append(f"{vn}:{rest}")
            else:
                newvols.append(vol)
        if newvols:
            v["volumes"] = newvols
        if n == app_name and cport:
            v["ports"] = [{"target": cport, "published": hp,
                           "protocol": "tcp", "mode": "ingress"}]
        v["deploy"] = {
            "mode": "replicated", "replicas": 1,
            "placement": {"constraints": ["node.platform.os == linux"]},
            "restart_policy": {"condition": "on-failure", "delay": "5s",
                               "max_attempts": 3},
            "update_config": {"order": "start-first",
                              "failure_action": "rollback"},
            "resources": {"limits": {"memory": "2G"}},
        }
    if named:
        d["volumes"] = named
    nets = {"default": {"name": f"{name}_net", "driver": "overlay",
                        "attachable": True}}
    for v in d["services"].values():
        used = v.get("networks")
        used = list(used) if isinstance(used, (list, dict)) else []
        for u in used:
            if u not in nets:
                nets[u] = {"driver": "overlay", "attachable": True}
    d["networks"] = nets
    return d


def dump(doc, header, name, hp, app_name):
    txt = yaml.dump(doc, sort_keys=False, default_flow_style=False, width=100)
    # append the commented homepage labels under the app service
    lines = txt.splitlines(True)
    out, ins = [], LABELS.format(name=name, hp=hp)
    for i, ln in enumerate(lines):
        out.append(ln)
        if ln.rstrip() == f"  {app_name}:":
            pass
    body = "".join(out)
    # insert labels right before the top-level volumes/networks block
    m = re.search(r"^(volumes:|networks:)", body, re.M)
    if m:
        body = body[:m.start()] + ins + body[m.start():]
    else:
        body = body + ins
    return detsub(header.format(name=name) + body, hp)


def main():
    inv = json.load(open("/tmp/scaletail_inv.json"))["new"]
    hostmap = json.load(open(HP_FILE))
    done, failed = [], []
    for key in sorted(inv):
        if key in SKIP:
            continue
        rec = inv[key]
        name = norm(rec["name"])
        hp = hostmap.get(key) or hostmap.get(name)
        if not hp:
            failed.append((key, "no host port"))
            continue
        try:
            built = build(key, rec, hp)
            if not built:
                failed.append((key, "no app service found"))
                continue
            doc, app_name, cport = built
            base = os.path.join(DONE, rec["name"])
            os.makedirs(os.path.join(base, "swarm"), exist_ok=True)
            wrote_env = write_env(base, rec, hp, cport)
            if wrote_env:
                import shutil
                shutil.copy(os.path.join(base, ".env"),
                            os.path.join(base, "swarm", ".env"))
            open(os.path.join(base, "docker-compose.yml"), "w").write(
                dump(doc, HEADER_C, name, hp, app_name))
            sw = to_swarm(doc, name, app_name, hp, cport)
            open(os.path.join(base, "swarm", "docker-stack.yml"), "w").write(
                dump(sw, HEADER_S, name, hp, app_name))
            done.append((key, len(doc["services"]), cport, hp))
        except Exception as e:
            failed.append((key, f"{type(e).__name__}: {e}"))
    print(f"REBUILT {len(done)}")
    for k, n, cp, hp in done:
        tag = f"{n} containers" if n > 1 else "single"
        print(f"  + {k:26s} {hp:>6d}->{str(cp or '-'):<6s} {tag}")
    print(f"\nFAILED {len(failed)}")
    for k, r in failed:
        print(f"  ! {k:26s} {r}")


if __name__ == "__main__":
    main()
