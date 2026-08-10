#!/usr/bin/env python3
"""Rebuild resolved.json: validate every image, upgrade fabricated ones.

For each service: take the on-disk image. If it's a fabricated <folder>/<folder>
pattern OR fails registry check, resolve a real image from imagemap.candidates()
(CURATED first, then heuristics). Writes resolved.json keyed by service name.
"""
import os, re, json, sys, concurrent.futures as cf
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import regcheck, imagemap

TOOLS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TOOLS)
DESKTOP = os.path.dirname(ROOT)
H2 = os.path.join(DESKTOP, "self-hosted-2")
DONE = ROOT


def disk_image(b):
    cf = os.path.join(b, "docker-compose.yml")
    if not os.path.exists(cf):
        return None
    m = re.search(r"^    image: (\S+)", open(cf).read(), re.M)
    return m.group(1) if m else None


def is_fabricated(name, img):
    if not img:
        return True
    if re.match(rf"^{re.escape(name)}/{re.escape(name)}:latest$", img):
        return True
    if img in ("alpine:3.20",) and name not in imagemap.CURATED:
        return False  # explicit scaffold, keep
    return False


services = {}
for root in (DONE, H2):
    if not os.path.isdir(root):
        continue
    for d in sorted(os.listdir(root)):
        b = os.path.join(root, d)
        img = disk_image(b)
        if img and d not in services:
            services[d] = {"image": img, "root": os.path.basename(root)}


def resolve_one(name, current):
    """Return a verified image for `name`, preferring current if it's real."""
    if current and not is_fabricated(name, current) and regcheck.check(current) == "OK":
        return current
    for cand in imagemap.candidates(name):
        if regcheck.check(cand) == "OK":
            return cand
    return current  # give up but keep what we had


with cf.ThreadPoolExecutor(16) as ex:
    futs = {d: ex.submit(resolve_one, d, v["image"]) for d, v in services.items()}
    resolved = {}
    for d, f in futs.items():
        new = f.result()
        resolved[d] = {"image": new, "root": services[d]["root"],
                       "upgraded": new != services[d]["image"]}

json.dump({"resolved": resolved}, open(os.path.join(TOOLS, "resolved.json"), "w"), indent=1)
upg = [d for d, v in resolved.items() if v.get("upgraded")]
print(f"resolved.json: {len(resolved)} services, {len(upg)} upgraded from fabricated/bad")
for d in upg[:30]:
    print(f"  {d}: {services[d]['image']} -> {resolved[d]['image']}")
