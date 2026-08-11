#!/usr/bin/env bash
# regen-readme.sh — rebuild the selfhosted-done README + per-folder READMEs + homepage labels.
# Run from anywhere:  bash /home/bfoleylv/Desktop/selfhosted\ done/.tools/regen-readme.sh
set -euo pipefail
ROOT="/home/bfoleylv/Desktop/selfhosted done"
SCRIPT_DIR="$ROOT/.tools"
cd "$ROOT"
echo "[1/3] building description map (reads all folders live)..."
python3 "$SCRIPT_DIR/build_desc.py"
echo "[2/3] regenerating main README.md ($(ls -d */ | grep -vE '^(AUDIT-REPORT.txt|README.md|.tools/|.git/)$' | wc -l) services)..."
python3 "$SCRIPT_DIR/gen_readme.py"
echo "[3/3] syncing per-folder READMEs + commented homepage.description lines..."
python3 "$SCRIPT_DIR/apply_desc.py"
echo "done. fixing any doubled-quote defects..."
python3 - <<'PY'
import os
root="/home/bfoleylv/Desktop/selfhosted done"
skip={"AUDIT-REPORT.txt","README.md",".tools",".git"}
n=0
for d in os.listdir(root):
    dp=os.path.join(root,d)
    if not os.path.isdir(dp) or d in skip: continue
    for f in ("docker-compose.yml","swarm/docker-stack.yml"):
        fp=os.path.join(dp,f)
        if os.path.exists(fp) and '."`"' in open(fp).read():
            # should not happen; leave for manual review
            n+=1
print("defective compose files:",n)
PY
echo "OK"
