#!/usr/bin/env bash
# Validate every ScaleTail-sourced service: compose + swarm, real errors only.
cd "$HOME/Desktop/selfhosted done" || exit 1
LIST=$(python3 - <<'PY'
import json
inv = json.load(open('/tmp/scaletail_inv.json'))['new']
skip = {'docker-socket-with-tailscale', 'homelab-h1', 'musicseerr',
        'tailscale-app-connector-node', 'tailscale-exit-node',
        'tailscale-subnet-router-node'}
print('\n'.join(v['name'] for k, v in sorted(inv.items()) if k not in skip))
PY
)
f=0; s=0; : > /tmp/v3.log
for d in $LIST; do
  o=$(cd "$d" && docker compose -f docker-compose.yml config -q 2>&1 \
        | grep -v "level=warning" | grep -v "^time=")
  [ -n "$o" ] && { echo "C $d: $o" >> /tmp/v3.log; f=$((f+1)); }
  o=$(cd "$d/swarm" && docker compose -f docker-stack.yml config -q 2>&1 \
        | grep -v "level=warning" | grep -v "^time=")
  [ -n "$o" ] && { echo "S $d: $o" >> /tmp/v3.log; s=$((s+1)); }
done
echo "REAL compose errors: $f   REAL swarm errors: $s"
cat /tmp/v3.log
echo "tailnet refs left: $(grep -rl '\.ts\.net\|\${TS_\|TAILNET' \
  --include=docker-compose.yml --include=docker-stack.yml . | wc -l)"
