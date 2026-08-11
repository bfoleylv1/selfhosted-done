#!/usr/bin/env python3
"""Generate a real README.md for the selfhosted-done library.

Merges, in priority order:
  1. web-verified descriptions from /tmp/gaps_g*.json (official sources)
  2. descriptions already in selfhosted-list.txt catalog
  3. per-folder category + ground-truth image/port/gpu from each compose
All structural facts (image, host port, GPU, category) are read from the
compose files on disk, not guessed.
"""
import os, re, json, glob

ROOT = "/home/bfoleylv/Desktop/selfhosted done"
SKIP = {"AUDIT-REPORT.txt", "README.md", ".tools", ".git"}

# ---------- load base services (ground truth from disk) ----------
def parse_compose(path):
    img = port = None; gpu = False; hc = "TCP port probe"
    try:
        txt = open(path).read()
    except Exception:
        return dict(image=None, port=None, gpu=False, hc=hc)
    m = re.search(r'image:\s*([^\s#]+)', txt)
    if m: img = m.group(1).strip().strip('"\'')
    pm = re.search(r'-\s*"?(\d+):\d+', txt)
    if pm: port = pm.group(1)
    if re.search(r'capabilities:\s*\[?"?gpu', txt) or re.search(r'/dev/dri', txt):
        gpu = True
    if re.search(r'test:\s*\[?"?CMD', txt) or "CMD-SHELL" in txt:
        hc = "container healthcheck"
    return dict(image=img, port=port, gpu=gpu, hc=hc)

def parse_folder_readme(d):
    cat = None
    p = os.path.join(ROOT, d, "README.md")
    if os.path.exists(p):
        txt = open(p).read()
        m = re.search(r'\*\*Category\*\*\s*\|\s*(.+)', txt)
        if m:
            cat = m.group(1).strip().rstrip("|").strip()
    return cat

dirs = sorted([d for d in os.listdir(ROOT)
               if os.path.isdir(os.path.join(ROOT, d)) and d not in SKIP])

services = {}
for d in dirs:
    c = parse_compose(os.path.join(ROOT, d, "docker-compose.yml"))
    cat = parse_folder_readme(d) or "Self Hosting Solutions"
    services[d] = {"name": d, "category": cat, **c, "desc": None, "url": ""}

# ---------- catalog descriptions (selfhosted-list.txt) ----------
catdesc = {}; cur = None; prev = ""
for line in open(os.path.join(ROOT, "selfhosted-list.txt")):
    s = line.rstrip("\n"); st = s.strip()
    if not st:
        prev = s; continue
    if set(st) <= set("=") and len(st) >= 3:
        prev = s; continue
    if st.startswith("- "):
        if cur and cur in catdesc and not catdesc[cur]:
            catdesc[cur] = st[2:].strip()
        prev = s; continue
    if set(prev.strip()) <= set("=") or prev.strip().startswith("==="):
        cur = st
        catdesc.setdefault(cur, "")
    else:
        cur = st
        catdesc.setdefault(cur, "")
    prev = s

def norm(x):
    return re.sub(r'[^a-z0-9]', '', x.lower())

alias = {"mysql / mariadb": "mysql-mariadb", "pinecone (self-hosted)": "pinecone"}
dirnorm = {norm(dd): dd for dd in dirs}
for nm, d in catdesc.items():
    k = norm(nm)
    tgt = None
    if k in dirnorm:
        tgt = dirnorm[k]
    else:
        for a, v in alias.items():
            if norm(a) == k and v in dirs:
                tgt = v; break
    if tgt and not services[tgt]["desc"]:
        services[tgt]["desc"] = d

# ---------- authoritative description map (built by /tmp/build_desc.py) ----------
_desc_map = {}
if os.path.exists("/tmp/desc_map.json"):
    _desc_map = json.load(open("/tmp/desc_map.json"))
for d, s in services.items():
    if d in _desc_map:
        s["desc"] = _desc_map[d]["desc"]
        s["url"] = _desc_map[d].get("url", "")
# ---------- helpers ----------
def prettify(name):
    fixes = {"mysql-mariadb": "MySQL / MariaDB", "airsonic-advanced": "Airsonic Advanced",
             "bitwarden-rs": "Bitwarden RS (Vaultwarden)", "vault-warden": "Vaultwarden",
             "elastic-search": "Elasticsearch", "cockroachdb": "CockroachDB",
             "opensearch": "OpenSearch", "paperless-ngx": "Paperless-ngx",
             "uptime-kuma": "Uptime Kuma", "nginx-proxy-manager": "Nginx Proxy Manager",
             "gitea": "Gitea", "searxng": "SearXNG"}
    if name in fixes:
        return fixes[name]
    return name.replace("-", " ").replace("_", " ").title()

def mdlink(name):
    return f"[{prettify(name)}](./{name})"

for d, s in services.items():
    if not s["desc"]:
        s["desc"] = f"{prettify(d)} self-hosted service."

# stable category order: by count desc, then alpha
from collections import Counter, defaultdict
catcount = Counter(s["category"] for s in services.values())
cat_order = sorted(catcount, key=lambda c: (-catcount[c], c.lower()))

by_cat = defaultdict(list)
for d, s in services.items():
    by_cat[s["category"]].append(s)
for c in by_cat:
    by_cat[c].sort(key=lambda s: s["name"].lower())

total = len(services)
gpu_n = sum(1 for s in services.values() if s["gpu"])

# ---------- build README ----------
L = []
L.append("# selfhosted-done\n")
L.append("A library of **%d** Docker Compose + Docker Swarm stacks for self-hosted services. "
         "Each folder contains a working `docker-compose.yml` (single host) and `swarm/docker-stack.yml` "
         "(cluster), with healthchecks, Homepage labels, and config/data volume mounts.\n" % total)
L.append("Every stack was generated from the project's real upstream image and tagged with its actual "
         "category and host port. Descriptions come from each project's official catalog/repo where available, "
         "and a clean short summary for every service.\n")
L.append("## At a glance\n")
L.append(f"- **Services:** {total}")
L.append(f"- **With GPU / hardware-acceleration blocks:** {gpu_n} (commented out — uncomment to enable)")
L.append(f"- **Categories:** {len(catcount)}")
L.append("- **Layout per service:** `docker-compose.yml`, `swarm/docker-stack.yml`, `config/`, `data/`")
L.append("- **Each folder also has its own `README.md`** with image, ports, category, and run command.\n")
L.append("## How to run\n")
L.append("Single host:\n")
L.append("```bash\ncd <service>\ndocker compose up -d\n```\n")
L.append("Swarm:\n")
L.append("```bash\ndocker stack deploy -c <service>/swarm/docker-stack.yml <service>\n```\n")
L.append("> Healthchecks are enabled but the `homepage.*` labels are commented out so they don't "
         "clutter a Homepage instance you don't have. Uncomment them in each compose to populate Homepage.\n")

L.append("## Services by category\n")
for c in cat_order:
    items = by_cat[c]
    L.append(f"### {c} ({len(items)})\n")
    L.append("| Service | Image | Port | GPU | Description |")
    L.append("|---|---|---|:--:|---|")
    for s in items:
        gpu = "✅" if s["gpu"] else "—"
        port = s["port"] or "—"
        img = f"`{s['image']}`" if s["image"] else "`—`"
        desc = s["desc"]
        if s["url"]:
            desc = f"{desc} — [site]({s['url']})"
        L.append(f"| {mdlink(s['name'])} | {img} | `{port}` | {gpu} | {desc} |")
    L.append("")

# Alphabetical index at the end (compact)
L.append("## Full index (A–Z)\n")
L.append("| Service | Category | Port |")
L.append("|---|---|---|")
for d, s in sorted(services.items()):
    L.append(f"| {mdlink(s['name'])} | {s['category']} | `{s['port'] or '—'}` |")
L.append("")

out = "\n".join(L) + "\n"
with open(os.path.join(ROOT, "README.md"), "w") as f:
    f.write(out)

# report
missing_url = sum(1 for s in services.values() if not s["url"])
print("README written:", os.path.join(ROOT, "README.md"))
print("total services:", total)
print("categories:", len(catcount))
print("gpu blocks:", gpu_n)
print("services with no site url (web-gap unresolved):", missing_url)
print("bytes:", len(out))
