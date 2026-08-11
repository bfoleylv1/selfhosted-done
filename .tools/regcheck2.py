#!/usr/bin/env python3
"""Registry existence check that does NOT consume Docker Hub pull rate limit.

- Docker Hub  -> hub.docker.com/v2/repositories/<ns>/<repo>/tags/<tag>  (JSON API,
                 separate quota from the pull/manifest endpoint)
- ghcr / lscr / quay / others -> standard registry v2 token dance + HEAD manifest
                 (these registries do not enforce Docker's anonymous pull cap)

Returns OK / BAD / ERR:<reason>. ERR is transient and never cached.
"""
import json, os, sys, urllib.request, urllib.error, urllib.parse
import concurrent.futures as cf

TOOLS = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(TOOLS, "regcache2.json")
_cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}

ACCEPT = ",".join([
    "application/vnd.oci.image.index.v1+json",
    "application/vnd.oci.image.manifest.v1+json",
    "application/vnd.docker.distribution.manifest.list.v2+json",
    "application/vnd.docker.distribution.manifest.v2+json",
])
UA = "Mozilla/5.0 (compose-library-audit)"


def split_ref(ref):
    tag = "latest"
    body = ref
    if "@" in ref:
        body, tag = ref.split("@", 1)
    elif ":" in ref.rsplit("/", 1)[-1]:
        body, tag = ref.rsplit(":", 1)
    if "/" in body and ("." in body.split("/")[0] or ":" in body.split("/")[0]):
        host, repo = body.split("/", 1)
    else:
        host, repo = "docker.io", body
    if host in ("docker.io", "index.docker.io", "registry-1.docker.io"):
        host = "docker.io"
        if "/" not in repo:
            repo = "library/" + repo
    return host, repo, tag


def _get(url, headers=None, method="GET", timeout=25):
    req = urllib.request.Request(url, method=method,
                                 headers={"User-Agent": UA, **(headers or {})})
    return urllib.request.urlopen(req, timeout=timeout)


def check_hub(repo, tag):
    url = f"https://hub.docker.com/v2/repositories/{repo}/tags/{urllib.parse.quote(tag)}"
    try:
        with _get(url) as r:
            return "OK" if r.status == 200 else "BAD"
    except urllib.error.HTTPError as e:
        if e.code in (404, 401):
            return "BAD"
        if e.code == 429:
            return "ERR:RATELIMIT"
        return f"ERR:HTTP{e.code}"
    except Exception as e:
        return "ERR:" + type(e).__name__


def check_v2(host, repo, tag):
    base = f"https://{host}/v2/{repo}/manifests/{urllib.parse.quote(tag)}"
    try:
        try:
            with _get(base, {"Accept": ACCEPT}, "HEAD") as r:
                return "OK" if r.status == 200 else "BAD"
        except urllib.error.HTTPError as e:
            if e.code != 401:
                return "BAD" if e.code == 404 else f"ERR:HTTP{e.code}"
            auth = e.headers.get("WWW-Authenticate", "")
        parts = dict(kv.split("=", 1) for kv in
                     auth.split(" ", 1)[1].split(",") if "=" in kv)
        realm = parts.get("realm", "").strip('"')
        service = parts.get("service", "").strip('"')
        scope = parts.get("scope", f"repository:{repo}:pull").strip('"')
        q = urllib.parse.urlencode({"service": service, "scope": scope})
        with _get(f"{realm}?{q}") as r:
            tok = json.load(r)
        t = tok.get("token") or tok.get("access_token")
        with _get(base, {"Accept": ACCEPT, "Authorization": f"Bearer {t}"}, "HEAD") as r:
            return "OK" if r.status == 200 else "BAD"
    except urllib.error.HTTPError as e:
        if e.code in (404, 401, 403):
            return "BAD"
        if e.code == 429:
            return "ERR:RATELIMIT"
        return f"ERR:HTTP{e.code}"
    except Exception as e:
        return "ERR:" + type(e).__name__


def check(ref):
    if not ref or ref.startswith("$"):
        return "BAD"
    if ref in _cache:
        return _cache[ref]
    host, repo, tag = split_ref(ref)
    res = check_hub(repo, tag) if host == "docker.io" else check_v2(host, repo, tag)
    if host == "docker.io" and res == "BAD":
        res = check_v2("registry-1.docker.io", repo, tag)   # second opinion
    if not res.startswith("ERR"):
        _cache[ref] = res
    return res


def save():
    json.dump(_cache, open(CACHE, "w"), indent=0)


if __name__ == "__main__":
    refs = [l.strip() for l in (open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin)
            if l.strip()]
    with cf.ThreadPoolExecutor(10) as ex:
        for r, s in zip(refs, ex.map(check, refs)):
            print(f"{s:14s} {r}")
    save()
