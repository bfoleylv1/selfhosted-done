#!/usr/bin/env python3
"""Regenerate compose + swarm stack for every service folder.

Scans MULTIPLE roots (the main library plus any 'done'/review folders the user
moves services into) so a folder being relocated mid-run is never skipped.
Host ports are allocated globally across all roots so nothing collides, and are
sticky (stored in hostports.json) so moving a folder never reshuffles ports.
"""
import os, sys, json

TOOLS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TOOLS)            # selfhosted done (source of truth)
DESKTOP = os.path.dirname(ROOT)
# Self-hosted-2 is the folder being checked/migrated. Done is the destination.
H2 = os.path.join(DESKTOP, "self-hosted-2")
ROOTS = []
for r in (ROOT, H2):
    if os.path.isdir(r) and r not in ROOTS:
        ROOTS.append(r)


def load_resolved():
    p = os.path.join(TOOLS, "resolved.json")
    if os.path.exists(p):
        d = json.load(open(p))
        return d.get("resolved", {})
    return {}


def load_meta():
    root = os.path.dirname(TOOLS)
    meta = {}
    for lst in ("selfhosted-list.txt",):
        p = os.path.join(root, lst)
        if os.path.exists(p):
            for line in open(p):
                line = line.strip()
                if line.startswith("#") or "|" not in line:
                    continue
                parts = [x.strip() for x in line.split("|")]
                if len(parts) < 2:
                    continue
                name = parts[1].strip()
                if name:
                    meta[name.lower().replace(" ", "-")] = (
                        name, line, parts[2:] if len(parts) > 2 else [])
    return meta


R = load_resolved()
META = load_meta()

# (root, folder) pairs
items = []
for r in ROOTS:
    for d in sorted(os.listdir(r)):
        if os.path.isdir(os.path.join(r, d)) and not d.startswith("."):
            items.append((r, d))

RESERVED = {22, 25, 53, 80, 111, 143, 443, 445, 631, 993, 995, 3306, 5432, 6379}
HP_FILE = os.path.join(TOOLS, "hostports.json")

# Assignments are STICKY: a service keeps its port forever, so moving a folder
# between roots never reshuffles the library. Only new services get allocated.
hostmap = json.load(open(HP_FILE)) if os.path.exists(HP_FILE) else {}
names = [d for _, d in items]
hostmap = {k: v for k, v in hostmap.items() if k in names}
used = set(hostmap.values())

import facts
for d in names:                                  # prefer the real upstream port
    if d in hostmap:
        continue
    p, _h = facts.port_health(d)
    if p and p not in used and p not in RESERVED and p >= 1024:
        hostmap[d] = p
        used.add(p)

nxt = 20000
for d in names:                                  # everyone else gets 20000+
    if d in hostmap:
        continue
    while nxt in used:
        nxt += 1
    hostmap[d] = nxt
    used.add(nxt)

n = 0
for root, d in items:
    ent = R.get(d)
    img = ent["image"] if ent else None
    if not img:
        # fall back to image currently on disk
        cf = os.path.join(root, d, "docker-compose.yml")
        if os.path.exists(cf):
            import re
            m = re.search(r"^    image: (\S+)", open(cf).read(), re.M)
            img = m.group(1) if m else None
    if not img:
        print(f"  ! no image for {d} (skipped)")
        continue
    cport, hspec = facts.port_health(d)
    hport = hostmap[d]
    g = facts.gpu_class(d)
    disp, desc, cats = d, None, []
    if d in META:
        disp, _line, rest = META[d]
        desc = rest[0] if rest else None
        cats = rest[1].split(",") if len(rest) > 1 and rest[1] else []
    base = os.path.join(root, d)
    open(os.path.join(base, "docker-compose.yml"), "w").write(
        __import__("emit").compose(d, img, cport, hspec, g, desc, cats, hport))
    os.makedirs(os.path.join(base, "swarm"), exist_ok=True)
    open(os.path.join(base, "swarm", "docker-stack.yml"), "w").write(
        __import__("emit").swarm(d, img, cport, hspec, g, desc, cats, hport))
    old = os.path.join(base, "swarm", "docker-compose.yml")
    if os.path.exists(old):
        os.remove(old)
    # No config/ or data/ directories: mount points are declared in the compose
    # file (./config, ./data) but the dirs are created by the user at deploy
    # time, not shipped as empty placeholders.
    n += 1

json.dump(hostmap, open(os.path.join(TOOLS, "hostports.json"), "w"), indent=1)
print(f"roots scanned: {len(ROOTS)}")
for r in ROOTS:
    print(f"   {r}")
print(f"regenerated {n} services ({n*2} files)")
print(f"gpu blocks: {sum(1 for _, d in items if facts.gpu_class(d))}")
print(f"unique host ports: {len(set(hostmap.values()))}/{len(hostmap)}")
