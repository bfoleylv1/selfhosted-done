#!/usr/bin/env python3
"""Ad-hoc verification of ~/Desktop/self-hosted/.tools/ behaviour.

Not a project test suite - this repo has none. Each check exercises a specific
guarantee the generators are supposed to provide, and fails loudly otherwise.
"""
import os, re, sys, json, hashlib, subprocess, shutil, tempfile
import concurrent.futures as cf

ROOT = os.path.expanduser("~/Desktop/selfhosted done")
DESKTOP = os.path.dirname(ROOT)
DONE = ROOT
TOOLS = os.path.join(ROOT, ".tools")
sys.path.insert(0, TOOLS)

results = []


def check(name, fn):
    try:
        ok, detail = fn()
    except Exception as e:
        ok, detail = False, f"{type(e).__name__}: {e}"
    results.append((ok, name, detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}\n         {detail}")
    return ok


def services():
    out = []
    done = os.path.expanduser("~/Desktop/selfhosted done")
    for r in [done]:
        for n in sorted(os.listdir(r)):
            b = os.path.join(r, n)
            if (os.path.isdir(b) and not n.startswith(".")
                    and os.path.exists(os.path.join(b, "docker-compose.yml"))):
                out.append((r, n))
    return out


def read_compose(r, n):
    """Tolerate the user moving a folder between roots mid-run."""
    for root in [r, ROOT, DONE]:
        p = os.path.join(root, n, "docker-compose.yml")
        if os.path.exists(p):
            return open(p).read()
    return None


SVCS = services()
print(f"discovered {len(SVCS)} services\n")


# ---------------------------------------------------------------- regcheck
def t_regcheck():
    import regcheck
    live = {
        "jellyfin/jellyfin:latest": "OK",
        "postgres:16-alpine": "OK",
        "lscr.io/linuxserver/radarr:latest": "OK",   # lscr.io token realm
        "quay.io/keycloak/keycloak:latest": "OK",    # quay token realm
        "42links/42links:latest": "BAD",             # fabricated
        "nonexistentthing123/nope:latest": "BAD",    # fabricated
    }
    bad = []
    for ref, want in live.items():
        got = regcheck.check(ref)
        hit = (got == "OK") if want == "OK" else (got != "OK")
        if not hit:
            bad.append(f"{ref} -> {got} (wanted {want})")
    return not bad, ("6/6 refs classified correctly across "
                     "docker.io/lscr.io/quay.io" if not bad else "; ".join(bad))


def t_no_transient_cached():
    import regcheck
    stuck = [k for k, v in regcheck._cache.items()
             if v.startswith("ERR") or v in ("RATELIMIT", "UNKNOWN")]
    return not stuck, (f"cache clean, {len(regcheck._cache)} entries"
                       if not stuck else f"{len(stuck)} transient errors cached: {stuck[:3]}")


# ---------------------------------------------------------------- resolution
def t_every_image_resolved():
    """Every service resolves; alpine:3.20 only where it was deliberately curated."""
    import imagemap
    R = json.load(open(os.path.join(TOOLS, "resolved.json")))["resolved"]
    miss = [n for _, n in SVCS if n not in R]
    # a stub is only acceptable if alpine was an explicit curated choice
    stub = [n for _, n in SVCS
            if n in R and R[n]["image"] == "alpine:3.20"
            and "alpine:3.20" not in imagemap.CURATED.get(n, [])]
    return not miss and not stub, (
        f"all {len(SVCS)} services resolved; every alpine fallback is curated"
        if not miss and not stub else f"missing={miss[:5]} uncurated_stub={stub[:5]}")


def t_images_live():
    """Every image actually referenced on disk resolves OK in the registry."""
    import regcheck
    imgs = set()
    for r, n in SVCS:
        t = read_compose(r, n)
        if t is None:
            continue
        m = re.search(r"^    image: (\S+)", t, re.M)
        if m:
            imgs.add(m.group(1))
    bad = [i for i in sorted(imgs) if regcheck.check(i) != "OK"]
    return not bad, (f"{len(imgs)} distinct images, all pullable"
                     if not bad else f"{len(bad)} unavailable: {bad[:5]}")


# ---------------------------------------------------------------- facts
def t_facts():
    import facts
    want = {"jellyfin": (8096, "transcode"), "ollama": (11434, "compute"),
            "postgresql": (5432, None), "qemu": (None, "passthrough"),
            "miniflux": (8080, None), "vllm": (None, "compute")}
    bad = []
    for n, (port, g) in want.items():
        p, _h = facts.port_health(n)
        if port and p != port:
            bad.append(f"{n} port {p}!={port}")
        if facts.gpu_class(n) != g:
            bad.append(f"{n} gpu {facts.gpu_class(n)}!={g}")
    return not bad, ("ports + gpu classes correct for 6 probes"
                     if not bad else "; ".join(bad))


# ---------------------------------------------------------------- generators
def t_regen_idempotent():
    """regen.py must be a pure function of its inputs."""
    def snap():
        h = hashlib.sha256()
        for r, n in SVCS:
            for f in ("docker-compose.yml", "swarm/docker-stack.yml"):
                p = os.path.join(r, n, f)
                if os.path.exists(p):
                    h.update(open(p, "rb").read())
        return h.hexdigest()
    before = snap()
    p = subprocess.run([sys.executable, os.path.join(TOOLS, "regen.py")],
                       capture_output=True, text=True, timeout=600)
    if p.returncode != 0:
        return False, f"regen.py exited {p.returncode}: {p.stderr[-200:]}"
    after = snap()
    return before == after, ("re-running regen.py changed nothing (hash stable)"
                             if before == after else "regen.py is NOT idempotent")


def t_ports_unique():
    seen = {}
    for r, n in SVCS:
        t = read_compose(r, n)
        if t is None:
            continue
        m = re.search(r'^      - "(\d+):(\d+)"', t, re.M)
        if not m:
            return False, f"{n} has no published port"
        seen.setdefault(int(m.group(1)), []).append(n)
    dupes = {k: v for k, v in seen.items() if len(v) > 1}
    return not dupes, (f"{len(seen)} unique host ports, no collisions"
                       if not dupes else f"collisions: {list(dupes.items())[:3]}")


def t_readme_matches_compose():
    bad = []
    for r, n in SVCS:
        rd = os.path.join(r, n, "README.md")
        if not os.path.exists(rd):
            if read_compose(r, n) is None:
                continue          # moved mid-run
            bad.append(f"{n}: no README")
            continue
        t = read_compose(r, n)
        if t is None:
            continue
        m = open(rd).read()
        img = re.search(r"^    image: (\S+)", t, re.M).group(1)
        hp, cp = re.search(r'^      - "(\d+):(\d+)"', t, re.M).groups()
        if f"`{img}`" not in m:
            bad.append(f"{n}: image")
        if f"| **Host port** | `{hp}` |" not in m:
            bad.append(f"{n}: hport")
        if f"| **Container port** | `{cp}` |" not in m:
            bad.append(f"{n}: cport")
        gpu_c = ("GPU env" in t) or ("PASSTHROUGH" in t)
        if gpu_c != ("## Hardware acceleration" in m):
            bad.append(f"{n}: gpu")
        if ("nc -z" in t) != ("TCP port probe" in m):
            bad.append(f"{n}: healthcheck")
    return not bad, (f"{len(SVCS)} READMEs agree with their compose file"
                     if not bad else f"{len(bad)} mismatches: {bad[:5]}")


# ---------------------------------------------------------------- swarm rules
def t_swarm_rules():
    bad = []
    for r, n in SVCS:
        p = os.path.join(r, n, "swarm", "docker-stack.yml")
        if not os.path.exists(p):
            bad.append(f"{n}: missing")
            continue
        s = open(p).read()
        if "container_name:" in s:
            bad.append(f"{n}: container_name")
        if re.search(r"^      - \./", s, re.M):
            bad.append(f"{n}: relative bind")
        if f"{n}_config:" not in s:
            bad.append(f"{n}: no named volume")
        if "node.role == worker" in s:
            bad.append(f"{n}: worker-only constraint")
        if "replicas:" not in s:
            bad.append(f"{n}: no deploy block")
    return not bad, (f"{len(SVCS)} swarm files obey swarm constraints"
                     if not bad else f"{len(bad)} violations: {bad[:5]}")


# ---------------------------------------------------------------- docker
def t_compose_valid_all():
    """Full docker-engine validation of every file, both roots."""
    p = subprocess.run([sys.executable, os.path.join(TOOLS, "validate.py")],
                       capture_output=True, text=True, timeout=1200)
    m = re.search(r"checked (\d+) services / (\d+) files", p.stdout)
    f = re.search(r"FAILURES: (\d+)", p.stdout)
    if not m or not f:
        return False, f"unparseable validate.py output: {p.stdout[-200:]}"
    n, files, nf = int(m.group(1)), int(m.group(2)), int(f.group(1))
    covered = n == len(SVCS)
    return nf == 0 and covered, (
        f"{n} services / {files} files valid per docker engine"
        if nf == 0 and covered
        else f"failures={nf}, covered {n} of {len(SVCS)} services")


RE_CFG = re.compile(r"^(\s*)#(?!#)\s?(.*)$")


def t_gpu_uncomment():
    """Uncommenting a GPU variant must yield valid YAML AND actually activate it."""
    cases = [
        ("jellyfin", "Intel Quick Sync / VAAPI",
         "--- Intel Quick Sync / VAAPI  OR  AMD VAAPI ---", "LIBVA_DRIVER_NAME"),
        ("jellyfin", "NVIDIA NVENC/NVDEC",
         "--- NVIDIA NVENC/NVDEC (needs nvidia-container-toolkit) ---", "NVIDIA_VISIBLE_DEVICES"),
        ("vllm", "NVIDIA CUDA",
         "--- NVIDIA CUDA (needs nvidia-container-toolkit) ---", "NVIDIA_VISIBLE_DEVICES"),
        ("vllm", "Intel oneAPI / OpenVINO",
         "--- Intel oneAPI / OpenVINO (iGPU compute) ---", "ONEAPI_DEVICE_SELECTOR"),
        ("vllm", "AMD ROCm", "--- AMD ROCm ---", "HSA_OVERRIDE_GFX_VERSION"),
    ]
    bad, okn = [], 0
    for folder, env_hdr, key_hdr, marker in cases:
        froot = next((r for r in ROOTS if os.path.exists(
            os.path.join(r, folder, "docker-compose.yml"))), None)
        if froot is None:
            bad.append(f"{folder}: missing (moved/deleted)")
            continue
        src = open(os.path.join(froot, folder, "docker-compose.yml")).read().split("\n")
        out, mode = [], None
        for l in src:
            s = l.strip()
            if s == f"## {env_hdr}:":
                out.append(l); mode = "env"; continue
            if mode == "env":
                if RE_CFG.match(l) and s.startswith("# - "):
                    m = RE_CFG.match(l); out.append(m.group(1) + m.group(2)); continue
                mode = None
            if s == f"## {key_hdr}":
                out.append(l); mode = "key"; continue
            if mode == "key":
                if s.startswith("##") or not s:
                    mode = None; out.append(l); continue
                if RE_CFG.match(l):
                    m = RE_CFG.match(l); out.append(m.group(1) + m.group(2)); continue
                mode = None
            out.append(l)
        d = tempfile.mkdtemp(prefix="hermes-verify-gpu-")
        try:
            open(os.path.join(d, "docker-compose.yml"), "w").write("\n".join(out))
            p = subprocess.run(["docker", "compose", "config"], cwd=d,
                               capture_output=True, text=True, timeout=90)
            if p.returncode != 0:
                bad.append(f"{folder}/{env_hdr}: invalid YAML")
            elif marker not in p.stdout:
                bad.append(f"{folder}/{env_hdr}: parsed but {marker} not active")
            else:
                okn += 1
        finally:
            shutil.rmtree(d, ignore_errors=True)
    return not bad, (f"{okn}/5 GPU variants valid AND active when uncommented"
                     if not bad else "; ".join(bad))


def t_gpu_commented_by_default():
    """Shipped files must not have GPU config live."""
    bad = []
    for r, n in SVCS:
        t = read_compose(r, n)
        if t is None:
            continue
        for key in ("devices:", "runtime: nvidia", "group_add:", "privileged: true"):
            for line in t.split("\n"):
                if line.strip().startswith(key):
                    bad.append(f"{n}: live {key}")
    return not bad, ("no GPU/privileged config active in any shipped file"
                     if not bad else f"{len(bad)} live: {bad[:5]}")


# ---------------------------------------------------------------- audit
def t_documented_scripts():
    """Every .tools script MAINTENANCE.md names must exist and import cleanly."""
    import py_compile
    doc = open(os.path.join(ROOT, "MAINTENANCE.md")).read()
    refs = sorted(set(re.findall(r"\.tools/(\w+\.py)", doc))
                  | set(re.findall(r"\|\s*`(\w+\.py)`\s*\|", doc)))
    bad = []
    for f in refs:
        p = os.path.join(TOOLS, f)
        if not os.path.exists(p):
            bad.append(f"{f}: missing")
            continue
        try:
            py_compile.compile(p, doraise=True)
        except Exception:
            bad.append(f"{f}: syntax")
    return bool(refs) and not bad, (
        f"{len(refs)} documented scripts all present and compiling"
        if not bad else "; ".join(bad))


def t_docs_consistent():
    """SCAFFOLDS.md and the audit must agree on the scaffold count."""
    GENERIC = {"alpine:3.20", "php:8.2-apache", "php:8.2-fpm", "node:20-alpine",
               "python:3.11-slim", "debian:12-slim", "ubuntu:24.04",
               "ruby:3.3-alpine", "eclipse-temurin:17-jre", "golang:1.23-alpine",
               "nginx:alpine", "elixir:1.16-alpine",
               "mcr.microsoft.com/dotnet/aspnet:8.0"}
    live = 0
    for r, n in SVCS:
        t = read_compose(r, n)
        if t is None:
            continue
        m = re.search(r"^    image: (\S+)", t, re.M)
        if m and m.group(1) in GENERIC:
            live += 1
    sc = open(os.path.join(ROOT, "SCAFFOLDS.md")).read()
    listed = len(re.findall(r"^\| `", sc, re.M))
    ad = open(os.path.join(ROOT, "AUDIT-REPORT.txt")).read()
    m = re.search(r"generic base image\s*:\s*(\d+)", ad)
    audited = int(m.group(1)) if m else -1
    ok = live == listed == audited
    return ok, (f"scaffold count agrees: {live} on disk = SCAFFOLDS.md = audit"
                if ok else f"disk={live} scaffolds_md={listed} audit={audited}")


def t_audit_all_pass():
    p = subprocess.run([sys.executable, os.path.join(TOOLS, "audit.py")],
                       capture_output=True, text=True, timeout=600)
    if p.returncode != 0:
        return False, f"audit.py exited {p.returncode}"
    m = re.search(r"STRUCTURAL CHECKS: (\d+)/(\d+) passed", p.stdout)
    if not m:
        return False, "no summary line in audit output"
    got, tot = int(m.group(1)), int(m.group(2))
    return got == tot, f"audit.py reports {got}/{tot} structural checks"


# ---------------------------------------------------------------- published
def t_published_repo():
    d = tempfile.mkdtemp(prefix="hermes-verify-clone-")
    try:
        p = subprocess.run(["git", "clone", "-q", "--depth", "1",
                            "https://github.com/bfoleylv1/selfhosted-done", d],
                           capture_output=True, text=True, timeout=180)
        if p.returncode != 0:
            return False, f"anonymous clone failed: {p.stderr[-150:]}"
        svc = sorted(x for x in os.listdir(d)
                     if os.path.isdir(os.path.join(d, x)) and x != ".git")
        miss = [s for s in svc if not os.path.exists(os.path.join(d, s, "README.md"))]
        bad = []
        for s in svc[:6]:
            q = subprocess.run(["docker", "compose", "config", "-q"],
                               cwd=os.path.join(d, s), capture_output=True,
                               text=True, timeout=120)
            if q.returncode != 0:
                bad.append(s)
        ok = not miss and not bad and os.path.exists(os.path.join(d, "README.md"))
        return ok, (f"cloned anonymously: {len(svc)} services, all have READMEs, "
                    f"{min(6,len(svc))} spot-checked valid"
                    if ok else f"missing_readme={miss[:3]} invalid={bad[:3]}")
    finally:
        shutil.rmtree(d, ignore_errors=True)


print("REGISTRY")
check("regcheck classifies real vs fabricated images", t_regcheck)
check("no transient errors poisoning the cache", t_no_transient_cached)
check("every service resolves to a real image", t_every_image_resolved)
check("every image on disk is pullable", t_images_live)
print("\nFACTS + GENERATORS")
check("port/gpu facts correct", t_facts)
check("regen.py is idempotent", t_regen_idempotent)
check("host ports unique across both roots", t_ports_unique)
check("per-service READMEs match their compose", t_readme_matches_compose)
print("\nSWARM")
check("swarm files obey swarm constraints", t_swarm_rules)
print("\nDOCKER ENGINE")
check("compose+swarm valid (all services, both roots)", t_compose_valid_all)
check("GPU variants valid AND active when uncommented", t_gpu_uncomment)
check("GPU config inert by default", t_gpu_commented_by_default)
print("\nDOCS + AUDIT + PUBLISHED ARTEFACT")
check("documented scripts exist and compile", t_documented_scripts)
check("scaffold counts agree across docs", t_docs_consistent)
check("audit.py reports all checks passing", t_audit_all_pass)
check("published GitHub repo is usable", t_published_repo)

fail = [n for ok, n, _ in results if not ok]
print("\n" + "=" * 62)
print(f"{len(results)-len(fail)}/{len(results)} checks passed")
if fail:
    print("FAILED: " + ", ".join(fail))
print("=" * 62)
sys.exit(1 if fail else 0)
