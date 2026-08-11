# Wiki Js

Modern and powerful wiki app; built on Node.js with Vue.js frontend

| | |
|---|---|
| **Image** | `ghcr.io/requarks/wiki:2` |
| **Host port** | `20363` |
| **Container port** | `3000` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:3000/` |
| **Category** | Productivity |

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
```

## Check it is healthy

```bash
docker compose ps
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
