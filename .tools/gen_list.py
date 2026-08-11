#!/usr/bin/env python3
"""Regenerate selfhosted-list.txt from what is actually on disk.

The catalog used to be hand-maintained and drifted (284 services missing, and a
README claiming 557 when 635 existed). This rebuilds it from the service folders
themselves, preserving every human-written description already in the file so no
curated prose is lost.

Run after adding services:  python3 gen_list.py
"""
import os, re, sys, json
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIST = os.path.join(ROOT, "selfhosted-list.txt")
TOOLS = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, TOOLS)
from mkreadme_svc import pretty, load_desc          # noqa: E402


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def parse_existing(path):
    """Pull {normalised name: (display name, description, category)} out of the
    current catalog so curated wording survives a regeneration."""
    if not os.path.exists(path):
        return {}, {}
    entries, cats = {}, {}
    cur_cat, cur_name, prev = None, None, ""
    for line in open(path):
        s = line.rstrip("\n")
        st = s.strip()
        if set(st) <= set("=") and len(st) >= 3:
            prev = s
            continue
        if not st:
            prev = s
            continue
        if set(prev.strip()) <= set("=") and prev.strip():
            # a line fenced by '=' is a category header
            cur_cat = st
            prev = s
            continue
        if st.startswith("- "):
            if cur_name:
                k = norm(cur_name)
                text = st[2:].strip()
                # the catalog contains duplicate entries for the same service
                # with differing wording; keep the most informative one
                if k not in entries or len(text) > len(entries[k][1]):
                    entries[k] = (cur_name, text)
                    cats[k] = cur_cat
            prev = s
            continue
        cur_name = st
        prev = s
    return entries, cats


def category_of(d):
    p = os.path.join(ROOT, d, "README.md")
    if os.path.exists(p):
        m = re.search(r"\*\*Category\*\*\s*\|\s*(.+)", open(p).read())
        if m:
            return m.group(1).strip().rstrip("|").strip()
    return None


def main():
    old, oldcat = parse_existing(LIST)
    desc = load_desc()
    dirs = sorted(d for d in os.listdir(ROOT)
                  if os.path.isdir(os.path.join(ROOT, d)) and not d.startswith("."))

    by_cat = defaultdict(list)
    kept = added = 0
    for d in dirs:
        k = norm(d)
        name = old[k][0] if k in old else pretty(d)
        if d in desc and desc[d].get("desc"):
            text = desc[d]["desc"]
            added += 1
        elif k in old and old[k][1]:
            text = old[k][1]
            kept += 1
        else:
            # read the service's own README first line of prose
            rp = os.path.join(ROOT, d, "README.md")
            text = ""
            if os.path.exists(rp):
                for ln in open(rp).read().split("\n"):
                    ln = ln.strip()
                    if ln and not ln.startswith(("#", "|", "-", "*", "`")):
                        text = ln
                        break
            text = text or f"{pretty(d)} self-hosted service."
            added += 1
        cat = oldcat.get(k) or category_of(d) or "SELF HOSTING SOLUTIONS"
        by_cat[cat.upper()].append((name, text, d))

    out = ["SELF-HOSTED SERVICES CATALOG", "=" * 28, "",
           f"{len(dirs)} services. Each has a folder with docker-compose.yml, "
           "swarm/docker-stack.yml and README.md.",
           "Generated from the service folders on disk - do not hand-edit; "
           "run .tools/gen_list.py.", ""]
    for cat in sorted(by_cat, key=lambda c: (-len(by_cat[c]), c)):
        out += ["=" * 80, cat, "=" * 80, ""]
        for name, text, d in sorted(by_cat[cat], key=lambda x: x[0].lower()):
            out += [name, f"- {text}", f"  ./{d}", ""]

    # Catalog entries with no folder: desktop apps, SaaS proxies, bare-metal
    # distros and wishlist items. Kept so the curated prose is never lost.
    have = {norm(d) for d in dirs}
    orphans = [(v[0], v[1], oldcat.get(k) or "UNCATEGORISED")
               for k, v in old.items() if k not in have and v[1]]
    if orphans:
        out += ["=" * 80,
                f"NOT PACKAGED ({len(orphans)}) - no compose folder",
                "=" * 80, "",
                "Desktop/mobile apps, hosted SaaS, bare-metal distros and "
                "wishlist entries.", "Listed for reference; they are not "
                "containerised in this library.", ""]
        for name, text, cat in sorted(orphans, key=lambda x: x[0].lower()):
            out += [name, f"- {text}", f"  [{cat}]", ""]

    open(LIST, "w").write("\n".join(out) + "\n")
    print(f"catalog rebuilt: {len(dirs)} services, {len(by_cat)} categories")
    print(f"  descriptions kept from existing catalog : {kept}")
    print(f"  descriptions newly sourced              : {added}")
    print(f"  not-packaged entries preserved          : {len(orphans)}")


if __name__ == "__main__":
    main()
