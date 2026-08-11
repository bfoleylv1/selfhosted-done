#!/usr/bin/env python3
"""Generate a per-service README.md for every service folder.

Everything is read from the service's own compose file, so the doc cannot drift
from the config: image, host/container port, companion containers, healthcheck
style, whether a .env ships. Descriptions come from a curated map when known
(upstream project READMEs), never invented.

Run: python3 mkreadme_svc.py [--force]
"""
import json, os, re, sys, yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATCACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "categories.json")
DESC_FILES = [os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "descriptions.json"),
              "/tmp/scaletail_desc.json", "/tmp/desc_map.json",
              os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "desc_map.json")]

FIXES = {"mysql-mariadb": "MySQL / MariaDB", "adguardhome": "AdGuard Home",
         "adguardhome-sync": "AdGuard Home Sync", "paperless": "Paperless-ngx",
         "uptime-kuma": "Uptime Kuma", "stirlingpdf": "Stirling PDF",
         "it-tools": "IT-Tools", "cyberchef": "CyberChef",
         "open-webui": "Open WebUI", "home-assistant": "Home Assistant",
         "netbox": "NetBox", "xwiki": "XWiki", "nodered": "Node-RED",
         "miniqr": "Mini QR", "swingmx": "Swing Music", "seerr": "Seerr",
         "qbittorrent": "qBittorrent", "rustdesk-server": "RustDesk Server",
         "actual-budget": "Actual Budget", "beszel-hub": "Beszel Hub",
         "beszel-agent": "Beszel Agent", "bentopdf": "BentoPDF"}


def pretty(n):
    return FIXES.get(n) or n.replace("-", " ").replace("_", " ").title()


def load_desc():
    d = {}
    for f in DESC_FILES:
        if os.path.exists(f):
            try:
                raw = json.load(open(f))
            except Exception:
                continue
            for k, v in raw.items():
                d.setdefault(k, v if isinstance(v, dict) else {"desc": v})
    return d


def facts(cc):
    """Read ground truth out of the compose file."""
    y = yaml.safe_load(open(cc)) or {}
    svcs = y.get("services") or {}
    app, hp, cp = None, None, None
    for n, v in svcs.items():
        for p in (v.get("ports") or []):
            m = re.match(r'^"?(\d+):(\d+)', str(p))
            if m:
                app, hp, cp = n, m.group(1), m.group(2)
                break
        if app:
            break
    if not app:
        app = next(iter(svcs), None)
    v = svcs.get(app, {})
    hc = "none"
    test = str((v.get("healthcheck") or {}).get("test", ""))
    if test:
        m = re.search(r"https?://[^\s'\"|]+", test)
        hc = f"HTTP `{m.group(0)}`" if m else "command probe"
    return {
        "image": v.get("image", "(unset)"),
        "hostport": hp, "cport": cp, "app": app,
        "services": list(svcs), "healthcheck": hc,
        "gpu": bool(re.search(r"/dev/dri|capabilities:\s*\[?\"?gpu",
                              open(cc).read())),
    }


def gen(name, base, f, desc, url, cat="Self Hosting Solutions"):
    title = pretty(name)
    has_env = os.path.exists(os.path.join(base, ".env"))
    companions = [s for s in f["services"] if s != f["app"]]
    rows = [
        ("Image", f"`{f['image']}`"),
        ("Host port", f"`{f['hostport']}`" if f["hostport"] else "_none (headless)_"),
        ("Container port", f"`{f['cport']}`" if f["cport"] else "_n/a_"),
        ("Containers", str(len(f["services"]))
         + (f" (app + {', '.join(companions)})" if companions else "")),
        ("Healthcheck", f["healthcheck"]),
        ("Category", cat),
    ]
    if f["gpu"]:
        rows.append(("GPU", "hardware-acceleration block included (commented)"))
    if url:
        rows.append(("Upstream", url))

    body = [f"# {title}", ""]
    body.append(desc or f"Self-hosted service: {name}.")
    body += ["", "| | |", "|---|---|"]
    body += [f"| **{k}** | {v} |" for k, v in rows]
    body += ["", "## Run it", "", "Single host:", "", "```bash",
             "docker compose up -d", "```", ""]
    if f["hostport"]:
        body += [f"Then open <http://localhost:{f['hostport']}>.", ""]
    else:
        body += ["This service has no web UI; it runs headless.", ""]
    body += ["Swarm:", "", "```bash",
             f"docker stack deploy -c swarm/docker-stack.yml {name}", "```", ""]
    if has_env:
        body += ["## Configuration", "",
                 "Settings live in `.env` next to the compose file. Generated "
                 "secrets are already filled in and are stable across "
                 "regeneration.", ""]
    body += ["## Layout", "", "```", "docker-compose.yml        # single-host deployment",
             "swarm/docker-stack.yml    # swarm stack (named volumes, replicas, placement)"]
    if has_env:
        body.append(".env                      # configuration and generated secrets")
    body += ["```", "", "## Check it is healthy", "", "```bash",
             "docker compose ps", "```", "",
             "## Homepage", "",
             "[gethomepage](https://github.com/gethomepage/homepage) labels are "
             "included but commented out. Uncomment the `labels:` block in "
             "`docker-compose.yml` to enable autodiscovery.", ""]
    return "\n".join(body)


def main():
    force = "--force" in sys.argv
    desc = load_desc()
    # preserve the category already recorded in each folder README, otherwise a
    # --force regeneration flattens every service into one category
    prior_cat = {}
    for d in os.listdir(ROOT):
        rp = os.path.join(ROOT, d, "README.md")
        if os.path.exists(rp):
            m = re.search(r"\*\*Category\*\*\s*\|\s*(.+)", open(rp).read())
            if m:
                prior_cat[d] = m.group(1).strip().rstrip("|").strip()
    if os.path.exists(CATCACHE):
        for k, v in json.load(open(CATCACHE)).items():
            prior_cat.setdefault(k, v)
    json.dump(prior_cat, open(CATCACHE, "w"), indent=0)
    made = 0
    for d in sorted(os.listdir(ROOT)):
        b = os.path.join(ROOT, d)
        cc = os.path.join(b, "docker-compose.yml")
        if not os.path.isdir(b) or d.startswith(".") or not os.path.exists(cc):
            continue
        rp = os.path.join(b, "README.md")
        if os.path.exists(rp) and not force:
            continue
        e = desc.get(d) or {}
        try:
            f = facts(cc)
        except Exception:
            continue
        open(rp, "w").write(
            gen(d, b, f, e.get("desc"), e.get("url"), prior_cat.get(d) or
                e.get("category") or "Self Hosting Solutions"))
        made += 1
    print(f"generated {made} README.md files")
    return made


if __name__ == "__main__":
    sys.exit(0 if main() >= 0 else 1)
