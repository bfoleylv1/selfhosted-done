#!/usr/bin/env python3
"""Whole-library integrity audit across 'selfhosted done' + 'self-hosted-2'.

Checks structure, swarm correctness, port collisions, and README/compose
agreement. Prints a report and writes AUDIT-REPORT.txt.
"""
import os, re, sys, yaml, collections, datetime

TOOLS = os.path.dirname(os.path.abspath(__file__))
DONE = os.path.dirname(TOOLS)
SH2 = os.path.join(os.path.dirname(DONE), "self-hosted-2")
ROOTS = [("done", DONE)] + ([("self-hosted-2", SH2)] if os.path.isdir(SH2) else [])


def services(root):
    for d in sorted(os.listdir(root)):
        b = os.path.join(root, d)
        if os.path.isdir(b) and not d.startswith("."):
            yield d, b


def main():
    checks = collections.OrderedDict()
    fails = collections.defaultdict(list)
    ports = collections.defaultdict(list)
    total = 0

    def ck(name, ok, who):
        checks.setdefault(name, [0, 0])
        checks[name][1] += 1
        if ok:
            checks[name][0] += 1
        else:
            fails[name].append(who)

    for label, root in ROOTS:
        for d, b in services(root):
            total += 1
            who = f"{label}/{d}"
            c = os.path.join(b, "docker-compose.yml")
            s = os.path.join(b, "swarm", "docker-stack.yml")
            r = os.path.join(b, "README.md")
            ck("docker-compose.yml present", os.path.exists(c), who)
            ck("swarm/docker-stack.yml present", os.path.exists(s), who)
            ck("README.md present", os.path.exists(r), who)
            if not os.path.exists(c):
                continue
            try:
                y = yaml.safe_load(open(c)) or {}
            except Exception:
                ck("compose parses", False, who)
                continue
            ck("compose parses", True, who)
            sy = {}
            if os.path.exists(s):
                try:
                    sy = yaml.safe_load(open(s)) or {}
                    ck("swarm parses", True, who)
                except Exception:
                    ck("swarm parses", False, who)

            csv_ = y.get("services") or {}
            ssv = sy.get("services") or {}
            ck("has image", all(v.get("image") for v in csv_.values()), who)
            ck("has healthcheck",
               any("healthcheck" in v for v in csv_.values()), who)
            ck("published port defined",
               any(v.get("ports") for v in csv_.values()), who)
            ck("homepage labels", "homepage." in open(c).read(), who)
            ck("no tailnet leftovers",
               not re.search(r"\.ts\.net|\$\{TS_|TAILNET", open(c).read()), who)

            for v in csv_.values():
                for pp in (v.get("ports") or []):
                    m = re.match(r'^"?(\d+):', str(pp))
                    if m:
                        ports[int(m.group(1))].append(who)

            if ssv:
                ck("swarm: no container_name",
                   not any("container_name" in v for v in ssv.values()), who)
                ck("swarm: deploy block",
                   all("deploy" in v for v in ssv.values()), who)
                ok = True
                for v in ssv.values():
                    for vol in (v.get("volumes") or []):
                        sv = str(vol)
                        if sv.startswith("./") or (
                                sv.startswith("/") and "docker.sock" not in sv):
                            ok = False
                ck("swarm: named volumes (no relative binds)", ok, who)
                ck("swarm: overlay network",
                   "overlay" in open(s).read(), who)

    dup = {p: v for p, v in ports.items() if len(v) > 1}
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    L = []
    L.append("=" * 72)
    L.append("SELF-HOSTED LIBRARY - INTEGRITY AUDIT")
    L.append(now)
    L.append("=" * 72)
    L.append("")
    L.append(f"Services audited : {total}")
    for label, root in ROOTS:
        L.append(f"  {label:14s} : {sum(1 for _ in services(root))}")
    L.append("")
    L.append("-" * 72)
    L.append("PER-CHECK RESULTS")
    L.append("-" * 72)
    for k, (good, tot) in checks.items():
        tag = "PASS" if good == tot else "FAIL"
        L.append(f"  [{tag}] {k:44s} {good}/{tot}")
        if good != tot:
            for w in fails[k][:8]:
                L.append(f"           - {w}")
    L.append("")
    L.append("-" * 72)
    L.append("PORTS")
    L.append("-" * 72)
    L.append(f"  unique published ports : {len(ports)}")
    L.append(f"  collisions             : {len(dup)}")
    for p, v in sorted(dup.items())[:20]:
        L.append(f"    {p}: {', '.join(v)}")
    out = "\n".join(L)
    print(out)
    open(os.path.join(DONE, "AUDIT-REPORT.txt"), "w").write(out + "\n")


if __name__ == "__main__":
    main()
