#!/usr/bin/env python3
"""Full ScaleTail inventory: walk both copies, find every leaf service
(a dir containing compose.yaml / docker-compose.yml), note which of the
3 variants it has (sidecar / no-tailscale / swarm), resolve ${IMAGE_URL}
from the sibling .env, and diff against the existing library.
"""
import os, re, json

DRIVE = "/run/media/bfoleylv/b3e166c3-2cf2-4275-9711-683a2288d3bb"
COPIES = [
    ("sh", f"{DRIVE}/compose/self hosted/ScaleTail/services"),
    ("h1", f"{DRIVE}/compose/from home1/ScaleTail/services"),
]
DESK = "/home/bfoleylv/Desktop"
DONE = f"{DESK}/selfhosted done"
SH2 = f"{DESK}/self-hosted-2"
CF = ("compose.yaml", "compose.yml", "docker-compose.yml", "docker-compose.yaml")
VARIANT_DIRS = {"swarm", "no tailscale", "ts", "mine", "config"}


def norm(n):
    return n.lower().strip().replace(" ", "-").replace("_", "-")


def compose_in(d):
    for f in CF:
        p = os.path.join(d, f)
        if os.path.isfile(p):
            return p
    return None


def read_env(d):
    e = {}
    p = os.path.join(d, ".env")
    if os.path.isfile(p):
        for line in open(p, errors="replace"):
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            e[k.strip()] = v.split("#")[0].strip()
    return e


def images(path, env):
    txt = open(path, errors="replace").read()
    out = []
    for m in re.findall(r"^\s*image:\s*[\"']?([^\"'\s#]+)", txt, re.M):
        r = m
        for k, v in env.items():
            r = r.replace("${" + k + "}", v)
        r = re.sub(r"\$\{([A-Z_]+):-([^}]*)\}", r"\2", r)
        out.append(r)
    return out


def walk(root, tag, acc, depth=0):
    if depth > 2 or not os.path.isdir(root):
        return
    for d in sorted(os.listdir(root)):
        p = os.path.join(root, d)
        if not os.path.isdir(p) or d.startswith(".") or d in VARIANT_DIRS:
            continue
        cf = compose_in(p)
        if cf:
            env = read_env(p)
            key = norm(d)
            rec = {
                "name": d, "path": p, "copy": tag, "compose": cf,
                "swarm": os.path.isdir(os.path.join(p, "swarm")),
                "nots": os.path.isdir(os.path.join(p, "no tailscale")),
                "images": images(cf, env),
                "port": env.get("SERVICEPORT"),
                "image_url": env.get("IMAGE_URL"),
            }
            prev = acc.get(key)
            # prefer the copy that already has all 3 variants
            if not prev or (rec["swarm"] and not prev["swarm"]):
                acc[key] = rec
        else:
            walk(p, tag, acc, depth + 1)


acc = {}
for tag, root in COPIES:
    walk(root, tag, acc)

have = set()
for lib in (DONE, SH2):
    for d in os.listdir(lib):
        if os.path.isdir(os.path.join(lib, d)) and not d.startswith("."):
            have.add(norm(d))

new = {k: v for k, v in acc.items() if k not in have}
dup = sorted(k for k in acc if k in have)

json.dump({"all": acc, "new": new, "dupe": dup}, open("/tmp/scaletail_inv.json", "w"), indent=1)
print(f"ScaleTail leaf services (deduped across both copies): {len(acc)}")
print(f"  with swarm variant : {sum(1 for v in acc.values() if v['swarm'])}")
print(f"  with no-tailscale  : {sum(1 for v in acc.values() if v['nots'])}")
print(f"  already in library : {len(dup)}")
print(f"  NEW                : {len(new)}")
print("\n--- NEW (name | port | resolved image | has swarm) ---")
for k in sorted(new):
    v = new[k]
    real = [i for i in v["images"] if "tailscale/tailscale" not in i]
    print(f"{k:28s} {str(v['port'] or '-'):>6s}  {(real[0] if real else '?'):46s} sw={int(v['swarm'])}")
