#!/usr/bin/env python3
"""One command to make the library self-consistent after adding services.

Order matters: per-service READMEs first (the catalog and the top-level README
both read from them), then the catalog, then the top-level README, then audit.

    python3 sync.py              # refresh only what is missing
    python3 sync.py --force      # regenerate every per-service README too

Run this after ANY service is added, removed or renamed.
"""
import os, subprocess, sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
FORCE = "--force" in sys.argv

STEPS = [
    ("per-service READMEs", ["mkreadme_svc.py"] + (["--force"] if FORCE else [])),
    ("catalog (selfhosted-list.txt)", ["gen_list.py"]),
    ("top-level README.md", ["gen_readme.py"]),
    ("integrity audit", ["audit2.py"]),
]


def main():
    rc = 0
    for label, cmd in STEPS:
        print(f"\n=== {label} " + "=" * (52 - len(label)))
        r = subprocess.run([sys.executable] + cmd, cwd=TOOLS,
                           capture_output=True, text=True)
        tail = [l for l in r.stdout.strip().split("\n") if l][-14:]
        print("\n".join(tail))
        if r.returncode:
            rc = r.returncode
            print(f"!! {label} exited {r.returncode}")
            print(r.stderr.strip()[-400:])
    print("\nsync complete" if not rc else "\nsync finished WITH ERRORS")
    return rc


if __name__ == "__main__":
    sys.exit(main())
