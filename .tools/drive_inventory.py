#!/usr/bin/env python3
"""Inventory every service folder on the external drive, extract its images,
and diff against the existing library (selfhosted done + self-hosted-2).
"""
import os, re, json, yaml, sys

DRIVE = "/run/media/bfoleylv/b3e166c3-2cf2-4275-9711-683a2288d3bb"
DESK = "/home/bfoleylv/Desktop"
DONE = os.path.join(DESK, "selfhosted done")
SH2 = os.path.join(DESK, "self-hosted-2")

SOURCES = [
    ("scaletail_h1", f"{DRIVE}/compose/from home1/ScaleTail/services"),
    ("scaletail_sh", f"{DRIVE}/compose/self hosted/ScaleTail/services"),
    ("home1",        f"{DRIVE}/compose/from home1"),
    ("homelab",      f"{DRIVE}/compose/homelab"),
    ("hp",           f"{DRIVE}/compose/compose with hp"),
    ("awesome",      f"{DRIVE}/compose/self hosted/awesome-compose"),
]
SKIP_DIRS = {"ScaleTail", "go", "gopath", "shell", "osint-engine", "scripts",
             "templates", ".git", "config", "data"}
CFILES = ("docker-compose.yml", "docker-compose.yaml", "compose.yml", "compose.yaml")


def find_compose(d):
    # prefer a plain compose at the folder root; ScaleTail nests one level
    for f in CFILES:
        p = os.path.join(d, f)
        if os.path.isfile(p):
            return p
    for sub in sorted(os.listdir(d)):
        sp = os.path.join(d, sub)
        if os.path.isdir(sp) and sub not in ("no tailscale", "swarm", "ts"):
            for f in CFILES:
                p = os.path.join(sp, f)
                if os.path.isfile(p):
                    return p
    # last resort: the tailscale-free variant
    for sub in ("no tailscale",):
        for f in CFILES:
            p = os.path.join(d, sub, f)
            if os.path.isfile(p):
                return p
    return None


def images_of(path):
    try:
        txt = open(path, errors="replace").read()
    except Exception:
        return []
    return re.findall(r"^\s*image:\s*[\"']?([^\"'\s#]+)", txt, re.M)


def norm(n):
    return n.lower().strip().replace(" ", "-").replace("_", "-")


inv = {}
for tag, root in SOURCES:
    if not os.path.isdir(root):
        continue
    for d in sorted(os.listdir(root)):
        full = os.path.join(root, d)
        if not os.path.isdir(full) or d.startswith(".") or d in SKIP_DIRS:
            continue
        cf = find_compose(full)
        if not cf:
            continue
        key = norm(d)
        imgs = images_of(cf)
        rec = {"name": d, "src": cf, "source": tag, "images": imgs}
        if key not in inv:
            inv[key] = rec
        else:                       # keep the entry with more images / ScaleTail
            if len(imgs) > len(inv[key]["images"]):
                inv[key] = rec

have_done = {norm(d) for d in os.listdir(DONE)
             if os.path.isdir(os.path.join(DONE, d)) and not d.startswith(".")}
have_sh2 = {norm(d) for d in os.listdir(SH2)
            if os.path.isdir(os.path.join(SH2, d)) and not d.startswith(".")}
have = have_done | have_sh2

new = {k: v for k, v in inv.items() if k not in have}
dupe = {k: v for k, v in inv.items() if k in have}

json.dump({"new": new, "dupe": sorted(dupe)}, open("/tmp/drive_inv.json", "w"), indent=1)
print(f"drive service folders found : {len(inv)}")
print(f"  already in library (skip) : {len(dupe)}")
print(f"  NEW to add                : {len(new)}")
print(f"library: done={len(have_done)} sh2={len(have_sh2)}")
print("\n--- NEW ---")
for k in sorted(new):
    v = new[k]
    print(f"{k:32s} {len(v['images'])} img  [{v['source']}]  {v['images'][:2]}")
