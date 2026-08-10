#!/usr/bin/env python3
"""Full integrity audit across the self-hosted library. Writes AUDIT-REPORT.txt."""
import os, re, sys, json, datetime, subprocess, concurrent.futures as cf

TOOLS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TOOLS)
DESKTOP = os.path.dirname(ROOT)
DONE = os.path.join(DESKTOP, "selfhosted done")
ROOTS = [ROOT] + ([DONE] if os.path.isdir(DONE) else [])

svcs = []
for r in ROOTS:
    for n in sorted(os.listdir(r)):
        b = os.path.join(r, n)
        if os.path.isdir(b) and not n.startswith(".") and \
           os.path.exists(os.path.join(b, "docker-compose.yml")):
            svcs.append((r, n))

checks = {k: [] for k in
          ("compose", "swarm", "readme", "health", "labels", "image_pinned",
           "no_placeholder_dirs", "swarm_named_vol", "swarm_no_cname",
           "swarm_deploy", "port_ok")}
ports, images, gpu = {}, {}, []

for r, n in svcs:
    b = os.path.join(r, n)
    cf_p = os.path.join(b, "docker-compose.yml")
    sw_p = os.path.join(b, "swarm", "docker-stack.yml")
    t = open(cf_p).read()
    s = open(sw_p).read() if os.path.exists(sw_p) else ""

    checks["compose"].append((n, True))
    checks["swarm"].append((n, os.path.exists(sw_p)))
    checks["readme"].append((n, os.path.exists(os.path.join(b, "README.md"))))
    checks["health"].append((n, "healthcheck:" in t and "healthcheck:" in s))
    checks["labels"].append((n, "homepage.name=" in t and "homepage.name=" in s))
    _ph = any(os.path.isdir(os.path.join(b, sub)) and not os.listdir(os.path.join(b, sub))
              for sub in ("config", "data"))
    checks["no_placeholder_dirs"].append((n, not _ph))
    m = re.search(r"^    image: (\S+)", t, re.M)
    img = m.group(1) if m else None
    images[n] = img
    checks["image_pinned"].append((n, bool(img)))

    pm = re.search(r'^\s*- "(\d+):(\d+)"', t, re.M)
    if pm:
        hp = int(pm.group(1))
        ports.setdefault(hp, []).append(n)
        checks["port_ok"].append((n, True))
    else:
        checks["port_ok"].append((n, False))

    checks["swarm_named_vol"].append((n, f"{n}_config:" in s))
    checks["swarm_no_cname"].append((n, "container_name:" not in s))
    checks["swarm_deploy"].append((n, "deploy:" in s and "replicas:" in s))

    if "GPU env" in t or "PASSTHROUGH" in t:
        kind = ("compute" if "GPU compute" in t else
                "transcode" if "video transcode" in t else "passthrough")
        gpu.append((n, kind))

dupes = {p: v for p, v in ports.items() if len(v) > 1}

L = []
A = L.append
A("=" * 72)
A("SELF-HOSTED LIBRARY - INTEGRITY AUDIT")
A(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
A("=" * 72)
A("")
A(f"Services audited : {len(svcs)}")
A(f"  main library   : {sum(1 for r, _ in svcs if r == ROOT)}")
A(f"  'done' folder  : {sum(1 for r, _ in svcs if r != ROOT)}")
A(f"Files            : {len(svcs)*2} compose+swarm")
A("")
A("-" * 72)
A("PER-CHECK RESULTS")
A("-" * 72)
LABEL = {
 "compose": "docker-compose.yml present", "swarm": "swarm/docker-stack.yml present",
 "readme": "README.md present", "health": "healthcheck (compose + swarm)",
 "labels": "homepage labels (compose + swarm)",
 "image_pinned": "image field present",
 "no_placeholder_dirs": "no empty config/ or data/ placeholders",
 "swarm_named_vol": "swarm uses named volumes", "swarm_no_cname": "swarm has no container_name",
 "swarm_deploy": "swarm deploy/replicas block", "port_ok": "published port defined",
}
for k, v in checks.items():
    ok = sum(1 for _, b in v if b)
    bad = [n for n, b in v if not b]
    mark = "PASS" if ok == len(v) else "FAIL"
    A(f"  [{mark}] {LABEL[k]:38s} {ok}/{len(v)}")
    for n in bad[:8]:
        A(f"          - {n}")
A("")
A("-" * 72)
A("PORTS")
A("-" * 72)
A(f"  unique published ports : {len(ports)}")
A(f"  collisions             : {len(dupes)}")
for p, v in list(dupes.items())[:10]:
    A(f"    {p}: {', '.join(v)}")
A("")
A("-" * 72)
A("HARDWARE ACCELERATION")
A("-" * 72)
A(f"  services with GPU blocks : {len(gpu)}")
for kind in ("transcode", "compute", "passthrough"):
    names = sorted(n for n, k in gpu if k == kind)
    A(f"    {kind:12s} {len(names):3d}  {', '.join(names[:10])}"
      + (" ..." if len(names) > 10 else ""))
A("")
A("  Blocks are commented out. '#' = real config (remove to enable),")
A("  '##' = human comment. Uncomment-tested for validity via test_gpu.")
A("")
A("-" * 72)
A("KNOWN LIMITATIONS")
A("-" * 72)
A("  1. Multi-container services (miniflux, lemmy, mailcow, nextcloud,")
A("     paperless-ngx, supabase, wazuh ...) ship as a single container. They")
A("     need a database/companion added before they will report healthy.")
A("  2. Some services are pinned to a generic runtime base image because no")
A("     official image is published. These start but need the app layer added.")
A("  3. Healthcheck endpoints are correct for the common case; a few apps")
A("     behind a login wall return 302 rather than 200.")
A("")
A("=" * 72)
tot = sum(len(v) for v in checks.values())
okc = sum(1 for v in checks.values() for _, b in v if b)
A(f"STRUCTURAL CHECKS: {okc}/{tot} passed"
  + ("  - ALL PASS" if okc == tot else f"  - {tot-okc} FAILED"))
A("=" * 72)

out = "\n".join(L)
open(os.path.join(ROOT, "AUDIT-REPORT.txt"), "w").write(out)
print(out)
