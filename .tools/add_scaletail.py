#!/usr/bin/env python3
"""Add verified ScaleTail services into the 'selfhosted done' library.

Source of truth = /tmp/scaletail_inv.json (built by scaletail_inventory.py) plus
the registry verification in regcheck2.py. Only services whose real image
verifies OK are added. Each gets the standard library layout:

    <svc>/docker-compose.yml
    <svc>/swarm/docker-stack.yml
    <svc>/README.md

Host ports come from the shared sticky hostports.json so nothing collides with
the 674 services already allocated.
"""
import json, os, re, sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, TOOLS)
import emit, facts, regcheck2, mkreadme_svc          # noqa: E402

DONE = os.path.dirname(TOOLS)
DESK = os.path.dirname(DONE)
SH2 = os.path.join(DESK, "self-hosted-2")
HP_FILE = os.path.join(TOOLS, "hostports.json")

# images corrected after verification showed the ScaleTail default was dead
OVERRIDE = {
    "recyclarr": "ghcr.io/recyclarr/recyclarr:7",
    "swingmx":   "ghcr.io/swingmx/swingmusic:latest",
}
# pure Tailscale node helpers - not standalone web services
SKIP = {"tailscale-app-connector-node", "tailscale-exit-node",
        "tailscale-subnet-router-node", "docker-socket-with-tailscale",
        "musicseerr", "homelab-h1"}

RESERVED = {22, 25, 53, 80, 111, 143, 443, 445, 631, 993, 995, 3306, 5432, 6379}


def norm(n):
    return n.lower().strip().replace(" ", "-").replace("_", "-")


def pick_image(rec, key):
    if key in OVERRIDE:
        return OVERRIDE[key]
    for i in rec["images"]:
        if not i or i.startswith("$") or "tailscale/tailscale" in i:
            continue
        return i if ":" in i.rsplit("/", 1)[-1] else i + ":latest"
    return None


def main():
    inv = json.load(open("/tmp/scaletail_inv.json"))["new"]
    hostmap = json.load(open(HP_FILE))
    used = set(hostmap.values())

    existing = set()
    for lib in (DONE, SH2):
        for d in os.listdir(lib):
            if os.path.isdir(os.path.join(lib, d)) and not d.startswith("."):
                existing.add(norm(d))

    added, skipped, failed = [], [], []
    for key in sorted(inv):
        rec = inv[key]
        if key in SKIP:
            skipped.append((key, "not a standalone service"))
            continue
        if key in existing:
            skipped.append((key, "already in library"))
            continue
        img = pick_image(rec, key)
        if not img:
            failed.append((key, "no resolvable image"))
            continue
        st = regcheck2.check(img)
        if st != "OK":
            failed.append((key, f"image {img} -> {st}"))
            continue

        # container port: ScaleTail .env SERVICEPORT is authoritative
        cport = None
        if rec.get("port") and str(rec["port"]).isdigit():
            cport = int(rec["port"])
        if not cport:
            cport, _ = facts.port_health(key)
        fport, fhealth = facts.port_health(key)
        hspec = fhealth if fport == cport else "/"
        if cport in (53, 25565, 45876, 51820):     # non-HTTP
            hspec = None

        if key in hostmap:
            hp = hostmap[key]
        else:
            hp = cport if (cport and cport not in used
                           and cport not in RESERVED and cport >= 1024) else None
            if hp is None:
                hp = 20000
                while hp in used:
                    hp += 1
            hostmap[key] = hp
        used.add(hp)

        g = facts.gpu_class(key)
        base = os.path.join(DONE, rec["name"])
        os.makedirs(os.path.join(base, "swarm"), exist_ok=True)
        svc = norm(rec["name"])
        open(os.path.join(base, "docker-compose.yml"), "w").write(
            emit.compose(svc, img, cport, hspec, g, None, [], hp))
        open(os.path.join(base, "swarm", "docker-stack.yml"), "w").write(
            emit.swarm(svc, img, cport, hspec, g, None, [], hp))
        added.append((key, img, hp, cport))

    json.dump(hostmap, open(HP_FILE, "w"), indent=1)
    regcheck2.save()

    print(f"ADDED   {len(added)}")
    for k, i, hp, cp in added:
        print(f"  + {k:28s} {hp:>6d}->{str(cp or '-'):<6s} {i}")
    print(f"\nSKIPPED {len(skipped)}")
    for k, r in skipped:
        print(f"  - {k:28s} {r}")
    print(f"\nFAILED  {len(failed)}")
    for k, r in failed:
        print(f"  ! {k:28s} {r}")


if __name__ == "__main__":
    main()
