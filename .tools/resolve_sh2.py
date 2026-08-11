#!/usr/bin/env python3
"""Broad image resolver for the self-hosted-2 batch.

For each service, generate many candidate refs (curated first, then Docker Hub
search results, then heuristic patterns) and test each with
`docker manifest inspect`. Writes sh2_resolved.json.

Docker Hub search is used as a discovery source only -- every hit is still
verified against the registry before being accepted.
"""
import json, os, re, subprocess, sys, urllib.request, urllib.parse
import concurrent.futures as cf

TOOLS = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(TOOLS, "sh2_resolved.json")

# hand-curated, checked below like everything else
CURATED = {
    "affine":        ["ghcr.io/toeverything/affine-graphql:stable", "ghcr.io/toeverything/affine:stable"],
    "affine-ce":     ["ghcr.io/toeverything/affine:stable"],
    "autogpt":       ["significantgravitas/auto-gpt:latest", "ghcr.io/significant-gravitas/autogpt:latest"],
    "bagisto":       ["bagisto/bagisto:latest", "webkul/bagisto:latest"],
    "bruno":         ["ghcr.io/usebruno/bruno:latest", "usebruno/bruno:latest"],
    "canary-tokens": ["thinkst/canarytokens:latest", "ghcr.io/thinkst/canarytokens:latest"],
    "channeltube":   ["thewicklowwolf/channeltube:latest"],
    "chatbox":       ["ghcr.io/bin-huang/chatbox:latest"],
    "cline":         ["ghcr.io/cline/cline:latest"],
    "codex":         ["ghcr.io/openai/codex:latest"],
    "context7":      ["ghcr.io/upstash/context7-mcp:latest", "mcp/context7:latest"],
    "cookcli":       ["ghcr.io/cooklang/cookcli:latest", "cooklang/cookcli:latest"],
    "copyparty":     ["copyparty/ac:latest", "ghcr.io/9001/copyparty:latest"],
    "crush":         ["ghcr.io/charmbracelet/crush:latest", "charmcli/crush:latest"],
    "dietpi":        ["dietpi/dietpi:latest", "mrsheepsheep/dietpi:latest"],
    "django-wiki":   ["python:3.12-slim"],
    "ente":          ["ghcr.io/ente-io/server:latest"],
    "enigma-bbs":    ["ghcr.io/nuskooler/enigma-bbs:latest", "davestephens/enigma-bbs:latest"],
    "goose":         ["ghcr.io/block/goose:latest"],
    "goploader":     ["ghcr.io/depado/goploader:latest", "depado/goploader:latest"],
    "graphhopper":   ["israelhikingmap/graphhopper:latest", "graphhopper/graphhopper:latest"],
    "grimoire":      ["goniszewski/grimoire:latest"],
    "hermes-agent":  ["ghcr.io/nousresearch/hermes-agent:latest"],
    "huginn":        ["ghcr.io/huginn/huginn:latest", "huginn/huginn:latest"],
    "hyrax":         ["ghcr.io/samvera/hyrax:latest", "samvera/hyrax:latest"],
    "inspircd":      ["inspircd/inspircd-docker:latest"],
    "jina":          ["jinaai/jina:latest"],
    "jitsi-meet":    ["jitsi/web:latest"],
    "karakeep":      ["ghcr.io/karakeep-app/karakeep:release", "ghcr.io/hoarder-app/hoarder:release"],
    "kiwix-serve":   ["ghcr.io/kiwix/kiwix-serve:latest", "kiwix/kiwix-serve:latest"],
    "languagetool":  ["erikvl87/languagetool:latest", "silviof/docker-languagetool:latest"],
    "lila":          ["ghcr.io/lichess-org/lila-docker:latest"],
    "linkwarden":    ["ghcr.io/linkwarden/linkwarden:latest"],
    "lobe-hub":      ["lobehub/lobe-chat:latest"],
    "logseq":        ["ghcr.io/logseq/logseq-webapp:latest", "logseq/logseq-webapp:latest"],
    "matchering":    ["ghcr.io/sergree/matchering-web:latest", "sergree/matchering-web:latest"],
    "memos":         ["neosmemo/memos:stable", "ghcr.io/usememos/memos:stable"],
    "mindustry":     ["ich777/mindustry-server:latest"],
    "musikcube":     ["lscr.io/linuxserver/musikcube:latest"],
    "octobox":       ["octobox/octobox:latest", "ghcr.io/octobox/octobox:latest"],
    "opencedit":     ["ghcr.io/opencut-app/opencut:latest"],
    "openship":      ["ghcr.io/openshiporg/openship:latest", "openshiporg/openship:latest"],
    "openwa":        ["openwa/wa-automate:latest"],
    "organicmaps":   ["alpine:3.20"],
    "pastefy":       ["ghcr.io/interaapps/pastefy:latest", "interaapps/pastefy:latest"],
    "piqueserver":   ["piqueserver/piqueserver:latest"],
    "posting":       ["ghcr.io/darrenburns/posting:latest"],
    "recipesage":    ["julianpoy/recipesage-selfhost:latest"],
    "servas":        ["beromir/servas:latest"],
    "sillytavern":   ["ghcr.io/sillytavern/sillytavern:latest"],
    "simplex-chat":  ["simplexchat/smp-server:latest"],
    "slash":         ["yourselfhosted/slash:latest"],
    "strava":        ["robiningelbrecht/strava-statistics:latest"],
    "tailchat":      ["moonrailgun/tailchat:latest"],
    "teleport":      ["public.ecr.aws/gravitational/teleport-distroless:16",
                      "quay.io/gravitational/teleport:latest"],
    "tldraw":        ["ghcr.io/tldraw/tldraw:latest", "nginx:alpine"],
    "ttrss":         ["cthulhoo/ttrss-fpm-pgsql-static:latest", "lscr.io/linuxserver/tt-rss:latest"],
    "wayback":       ["wabarc/wayback:latest", "ghcr.io/wabarc/wayback:latest"],
    "yaade":         ["esperoj/yaade:latest"],
    "linkding":      ["sissbruecker/linkding:latest"],
}

HUB = "https://hub.docker.com/v2/search/repositories/?query={}&page_size=8"


def hub_search(term):
    try:
        req = urllib.request.Request(HUB.format(urllib.parse.quote(term)),
                                     headers={"User-Agent": "curl/8"})
        with urllib.request.urlopen(req, timeout=20) as r:
            d = json.load(r)
        out = []
        for it in d.get("results", []):
            n = it.get("repo_name")
            if not n:
                continue
            out.append(f"{n}:latest")
        return out
    except Exception:
        return []


def heur(name):
    short = name.replace("-", "")
    c = [
        f"{name}/{name}:latest",
        f"ghcr.io/{name}/{name}:latest",
        f"lscr.io/linuxserver/{name}:latest",
        f"linuxserver/{name}:latest",
        f"{name}:latest",
        f"{short}/{short}:latest",
        f"ghcr.io/{short}/{short}:latest",
        f"quay.io/{name}/{name}:latest",
    ]
    return c


_cachef = os.path.join(TOOLS, "sh2_regcache.json")
_cache = json.load(open(_cachef)) if os.path.exists(_cachef) else {}


def check(ref):
    if ref in _cache:
        return _cache[ref]
    try:
        p = subprocess.run(["docker", "manifest", "inspect", ref],
                           capture_output=True, text=True, timeout=45)
        res = "OK" if p.returncode == 0 else "BAD"
    except Exception as e:
        return "ERR:" + type(e).__name__
    _cache[ref] = res
    return res


def resolve(name):
    seen, cands = set(), []
    for c in CURATED.get(name, []) + hub_search(name) + heur(name):
        if c not in seen:
            seen.add(c)
            cands.append(c)
    for c in cands:
        if check(c) == "OK":
            return name, c, len(cands)
    return name, None, len(cands)


if __name__ == "__main__":
    names = [l.split()[0] for l in open("/tmp/sh2_images.txt")]
    res, unres = {}, []
    with cf.ThreadPoolExecutor(8) as ex:
        for n, img, tried in ex.map(resolve, names):
            if img:
                res[n] = img
                print(f"OK    {n:22s} {img}")
            else:
                unres.append(n)
                print(f"MISS  {n:22s} (tried {tried})")
    json.dump(_cache, open(_cachef, "w"), indent=0)
    json.dump({"resolved": res, "unresolved": unres}, open(OUT, "w"), indent=1)
    print(f"\nresolved {len(res)}/{len(names)}  unresolved {len(unres)}")
    print("unresolved:", " ".join(unres))
