#!/usr/bin/env python3
"""Validate every compose and swarm file with the real docker CLI."""
import os, subprocess, sys, concurrent.futures as cf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DONE = os.path.join(os.path.dirname(ROOT), "selfhosted done")
ROOTS = [ROOT] + ([DONE] if os.path.isdir(DONE) else [])


def live_root(d):
    """Resolve the current root for a service; tolerate it being moved mid-run."""
    for r in ROOTS:
        if os.path.exists(os.path.join(r, d, "docker-compose.yml")):
            return r
    return None


svcs = [d for r in ROOTS for d in sorted(os.listdir(r))
        if os.path.isdir(os.path.join(r, d)) and not d.startswith(".")
        and os.path.exists(os.path.join(r, d, "docker-compose.yml"))]


def run(args, cwd):
    p = subprocess.run(args, cwd=cwd, capture_output=True, text=True, timeout=120)
    err = "\n".join(l for l in p.stderr.splitlines()
                    if l.strip() and "version` is obsolete" not in l)
    return p.returncode, err


def check(d):
    root = live_root(d)
    if root is None:
        return []
    bad = []
    rc, err = run(["docker", "compose", "-f", "docker-compose.yml", "config", "-q"],
                  os.path.join(root, d))
    if rc != 0:
        bad.append(("compose", d, err[:300]))
    rc, err = run(["docker", "compose", "-f", "docker-stack.yml", "config", "-q"],
                  os.path.join(root, d, "swarm"))
    if rc != 0:
        bad.append(("swarm", d, err[:300]))
    return bad


fails = []
with cf.ThreadPoolExecutor(8) as ex:
    for r in ex.map(check, svcs):
        fails.extend(r)

print(f"checked {len(svcs)} services / {len(svcs)*2} files across {len(ROOTS)} root(s)")
print(f"FAILURES: {len(fails)}")
for kind, d, err in fails[:40]:
    print(f"  [{kind}] {d}: {err.splitlines()[0] if err else '?'}")
sys.exit(1 if fails else 0)
