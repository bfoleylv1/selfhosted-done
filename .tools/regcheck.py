#!/usr/bin/env python3
"""Image existence verifier using `docker manifest inspect` as the authority.

`docker manifest inspect <ref>` is the reliable oracle:
  rc == 0  -> image exists and is (anonymously) inspectable/pullable
  rc != 0  -> does not exist or not anonymously accessible -> treat as unavailable

This is more reliable than the registry HTTP API, which returns 401 (AUTHREQ)
for many real Docker Hub images that simply require `docker login`. The
manifest CLI handles auth transparently.

Results are cached in regcache.json. Network errors are NOT cached as permanent.
"""
import json, os, subprocess

CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "regcache.json")

_cache = {}
if os.path.exists(CACHE):
    try:
        _cache = json.load(open(CACHE))
    except Exception:
        _cache = {}


def _save():
    json.dump(_cache, open(CACHE, "w"))


def check(ref):
    if ref in _cache:
        return _cache[ref]
    try:
        r = subprocess.run(["docker", "manifest", "inspect", ref],
                           capture_output=True, text=True, timeout=60)
        ok = r.returncode == 0
        res = "OK" if ok else "BAD"
    except subprocess.TimeoutExpired:
        return "ERR:TIMEOUT"   # transient, not cached
    except Exception as e:
        return "ERR:" + type(e).__name__   # transient, not cached
    if res != "ERR":
        _cache[ref] = res
        _save()
    return res


if __name__ == "__main__":
    import sys, concurrent.futures as cf
    refs = sys.argv[1:]
    def one(r):
        return r, check(r)
    with cf.ThreadPoolExecutor(16) as ex:
        for r, c in ex.map(one, refs):
            print(f"{c:6s} {r}")
