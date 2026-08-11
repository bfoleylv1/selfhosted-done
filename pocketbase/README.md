# Pocketbase

Open-source backend (SQLite + realtime + auth) in a single file

| | |
|---|---|
| **Image** | `ghcr.io/muchobien/pocketbase:latest` |
| **Host port** | `8090` |
| **Container port** | `8090` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:8090/api/health` |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:8090>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml pocketbase
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
