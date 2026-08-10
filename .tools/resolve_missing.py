#!/usr/bin/env python3
"""Broad image resolver for self-hosted-2 services.

Tests many candidate patterns across Docker Hub, ghcr.io, quay.io, and
lscr.io. Updates resolved.json in place for names that resolve to a real,
anonymous-pullable image. Leaves unresolved names untouched (kept fabricated)
so they are visible in the audit rather than silently fixed.
"""
import os, re, json, sys, concurrent.futures as cf
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import regcheck, imagemap

TOOLS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TOOLS)
H2 = os.path.join(os.path.dirname(ROOT), "self-hosted-2")
R = json.load(open(os.path.join(TOOLS, "resolved.json")))["resolved"]


def candidates(name):
    out = list(imagemap.CURATED.get(name, []))
    base = [
        f"lscr.io/linuxserver/{name}:latest",
        f"{name}/{name}:latest",
        f"linuxserver/{name}:latest",
        f"ghcr.io/{name}/{name}:latest",
        f"ghcr.io/{name}-docker/{name}:latest",
        f"quay.io/{name}/{name}:latest",
    ]
    for c in base:
        if c not in out:
            out.append(c)
    return out


def first_ok(name):
    for c in candidates(name):
        if regcheck.check(c) == "OK":
            return c
    return None


# names whose cached image is still fabricated
fab = [d for d, v in R.items() if re.match(rf"^{re.escape(d)}/{re.escape(d)}:latest$", v["image"])]
print(f"fabricated names to resolve: {len(fab)}")
with cf.ThreadPoolExecutor(24) as ex:
    futs = {d: ex.submit(first_ok, d) for d in fab}
    found = {}
    for d, f in futs.items():
        r = f.result()
        if r:
            found[d] = r
print(f"resolved now: {len(found)}")
for d in fab:
    if d in found:
        R[d]["image"] = found[d]
        R[d]["upgraded"] = True
        print(f"  {d}: {found[d]}")
json.dump({"resolved": R}, open(os.path.join(TOOLS, "resolved.json"), "w"), indent=1)
still = [d for d, v in R.items() if re.match(rf"^{re.escape(d)}/{re.escape(d)}:latest$", v["image"])]
print(f"STILL fabricated: {len(still)}")
for d in still:
    print("  ", d)
