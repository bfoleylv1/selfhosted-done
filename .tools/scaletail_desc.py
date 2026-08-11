#!/usr/bin/env python3
"""Extract a real one-line description for each ScaleTail service.

Upstream ships a README.md per service; the first prose sentence that describes
the project (not the Tailscale wrapper) is a far better description than
"<Name> self-hosted service." Falls back to nothing rather than inventing text.

Writes /tmp/scaletail_desc.json  ->  {service: {"desc": ..., "url": ...}}
"""
import json, os, re

inv = json.load(open("/tmp/scaletail_inv.json"))["new"]
SKIP = {"tailscale-app-connector-node", "tailscale-exit-node",
        "tailscale-subnet-router-node", "docker-socket-with-tailscale",
        "musicseerr", "homelab-h1"}

out = {}
for key, rec in sorted(inv.items()):
    if key in SKIP:
        continue
    p = os.path.join(rec["path"], "README.md")
    if not os.path.isfile(p):
        continue
    txt = open(p, errors="replace").read()

    # the section named after the project holds its real description
    url = ""
    m = re.search(r"\[([^\]]+)\]\((https?://github\.com/[^\)]+)\)", txt)
    if m:
        url = m.group(2)

    desc = ""
    # prefer the paragraph under the "## <Project>" heading
    sec = re.split(r"^##\s+", txt, flags=re.M)
    for chunk in sec[1:]:
        head, _, body = chunk.partition("\n")
        if "tailscale" in head.lower() or "sidecar" in head.lower():
            continue
        for para in body.split("\n\n"):
            s = " ".join(para.split()).strip()
            if len(s) > 60 and not s.startswith(("|", "-", "*", "#", "```")):
                desc = s
                break
        if desc:
            break

    if not desc:                      # fall back to the intro paragraph
        for para in txt.split("\n\n")[1:4]:
            s = " ".join(para.split()).strip()
            if len(s) > 60 and not s.startswith(("|", "-", "*", "#", "```")):
                desc = s
                break
    if not desc:
        continue

    desc = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", desc)      # unlink
    desc = re.sub(r"\*\*([^*]+)\*\*", r"\1", desc)                # unbold
    desc = re.sub(r"[*_`]", "", desc)                            # stray md
    desc = re.sub(r"\s+", " ", desc).strip()
    # first sentence, capped
    m = re.match(r"(.{40,300}?[.!])\s", desc + " ")
    if m:
        desc = m.group(1)
    if len(desc) > 300:
        desc = desc[:297].rsplit(" ", 1)[0] + "..."
    # drop tailscale-wrapper framing
    if re.search(r"tailscale sidecar|this docker compose configuration",
                 desc, re.I):
        continue
    out[rec["name"]] = {"desc": desc, "url": url}

json.dump(out, open("/tmp/scaletail_desc.json", "w"), indent=1)
print(f"descriptions extracted: {len(out)}")
for k in list(sorted(out))[:6]:
    print(f"  {k:20s} {out[k]['desc'][:88]}")
