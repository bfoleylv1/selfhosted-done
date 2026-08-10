# Wiki.js

Modern and powerful wiki app; built on Node.js with Vue.js frontend

| | |
|---|---|
| **Image** | `ghcr.io/requarks/wiki:2` |
| **Host port** | `20363` |
| **Container port** | `3000` |
| **Category** | Productivity |
| **Healthcheck** | HTTP `/healthz` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20363>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml wiki-js
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
docker inspect --format '{{.State.Health.Status}}' wiki-js
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
