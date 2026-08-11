#!/usr/bin/env python3
"""Build a single authoritative desc_map for all 518 services.

Priority: verified-GitHub (real matching selfhosted repo) >
           selfhosted-list.txt catalog > per-folder README prose >
           best-knowledge file > generic fallback.
No flags are emitted; every service gets a clean one-line description.
URLs are attached only where a real matching repo was verified.
"""
import os, re, json

ROOT = "/home/bfoleylv/Desktop/selfhosted done"
SKIP = {"AUDIT-REPORT.txt", "README.md", ".tools", ".git"}
dirs = sorted([d for d in os.listdir(ROOT)
               if os.path.isdir(os.path.join(ROOT, d)) and d not in SKIP])

def norm(x):
    return re.sub(r'[^a-z0-9]', '', x.lower())

# ---- catalog ----
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
        cur = st; catdesc.setdefault(cur, "")
    else:
        cur = st; catdesc.setdefault(cur, "")
    prev = s

alias = {"mysql / mariadb": "mysql-mariadb", "pinecone (self-hosted)": "pinecone"}
dirnorm = {norm(dd): dd for dd in dirs}
catalog = {}
for nm, d in catdesc.items():
    k = norm(nm); tgt = None
    if k in dirnorm: tgt = dirnorm[k]
    else:
        for a, v in alias.items():
            if norm(a) == k and v in dirs: tgt = v; break
    if tgt: catalog[tgt] = d

# ---- per-folder prose ----
placeholder_re = re.compile(r'self-?hosted service\.?$', re.I)
def pfr(d):
    p = os.path.join(ROOT, d, "README.md")
    if not os.path.exists(p): return None
    for line in open(p):
        st = line.strip()
        if st and not st.startswith("#"):
            return st
    return None

# ---- knowledge file ----
knowledge = json.load(open("/tmp/knowledge_gaps.json"))

# ---- verified github (real matching selfhosted repos) ----
verified = {
    "gomodel": ("GoModel: open-source AI gateway / control plane proxy with an OpenAI- and "
                "Anthropic-compatible API (a LiteLLM alternative).",
                "https://github.com/ENTERPILOT/GoModel"),
    "lms": ("Frappe LMS: 100% open-source learning management system.",
            "https://github.com/frappe/lms"),
    "openclaw": ("OpenClaw: self-hosted personal AI assistant (cross-platform).",
                 "https://github.com/openclaw/openclaw"),
    "txtdot": ("txtdot: HTTP proxy that strips pages down to text, links and images to save "
               "bandwidth and block ads/scripts.",
               "https://github.com/TempoWorks/txtdot"),
    "wagmios": ("Wagmios: give your AI agent a homelab (self-hosted agent tooling).",
                "https://github.com/mentholmike/wagmios"),
}

def clean(desc):
    # strip any leftover marker
    return desc.replace("⚠", "").strip()

desc_map = {}
for d in dirs:
    url = ""
    if d in verified:
        desc, url = verified[d]
    elif d in catalog and catalog[d]:
        desc = catalog[d]
    else:
        pd = pfr(d)
        if pd and not placeholder_re.search(pd):
            desc = pd
        elif d in knowledge:
            desc = knowledge[d]
        else:
            desc = f"{d.replace('-',' ').replace('_',' ').title()} self-hosted service."
    desc_map[d] = {"desc": clean(desc), "url": url}

json.dump(desc_map, open("/tmp/desc_map.json", "w"), indent=1)
verified_n = sum(1 for v in desc_map.values() if v["url"])
print("desc_map built for", len(desc_map), "services")
print("with verified URL:", verified_n)
# show the 28 previously-unknown now resolved
for n in ["crucial","daisy","docuddle","ekso","fmd-server","full-help","gomodel","gordian",
          "libervrt","lms","openclaw","phice","repo-flow","revent","revert","sama","seppo",
          "smederee","smite","supers3cret","surge","teikei","txtdot","wagmios","watchcode",
          "xcpg","zeit","zk-cloudserver"]:
    print(f"  {n:14s}: {desc_map[n]['desc'][:70]}")
