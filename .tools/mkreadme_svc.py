#!/usr/bin/env python3
"""Generate a per-service README.md for every service folder in ROOT.

Matches the established format: title, image, host/container port, category,
healthcheck, run instructions, layout, health check, homepage note.
Run: python3 mkreadme_svc.py
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PORT_RE = re.compile(r'^\s*-\s*"(\d+):\d+"', re.M)
IMG_RE = re.compile(r'^    image: (\S+)', re.M)
HCP_RE = re.compile(r'healthcheck:', re.M)

CATEGORY = "Self Hosting Solutions"  # default; list metadata not always present


def gen(name, cc_path, port):
    img_m = IMG_RE.search(open(cc_path).read())
    img = img_m.group(1) if img_m else "(unset)"
    health = "TCP/HTTP probe" if HCP_RE.search(open(cc_path).read()) else "none declared"
    return f"""# {name.title()}

Self-hosted service: {name}

| | |
|---|---|
| **Image** | `{img}` |
| **Host port** | `{port}` |
| **Container port** | `{port}` |
| **Category** | {CATEGORY} |
| **Healthcheck** | {health} |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:{port}>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml {name}
```

## Layout

```
docker-compose.yml        # single-host deployment
swarm/docker-stack.yml    # swarm stack (named volumes, replicas, placement)
config/                   # mounted to /config
data/                     # mounted to /data
```

## Check it is healthy

```bash
docker inspect --format '{{{{.State.Health.Status}}}}' {name}
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
"""


def main():
    made = 0
    for d in sorted(os.listdir(ROOT)):
        b = os.path.join(ROOT, d)
        cc = os.path.join(b, "docker-compose.yml")
        if not os.path.isdir(b) or d.startswith(".") or not os.path.exists(cc):
            continue
        if os.path.exists(os.path.join(b, "README.md")):
            continue
        t = open(cc).read()
        m = PORT_RE.search(t)
        port = m.group(1) if m else "8080"
        open(os.path.join(b, "README.md"), "w").write(gen(d, cc, port))
        made += 1
    print(f"generated {made} README.md files")
    return made


if __name__ == "__main__":
    sys.exit(0 if main() >= 0 else 1)
