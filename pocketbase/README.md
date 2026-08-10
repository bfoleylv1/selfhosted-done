# Pocketbase

pocketbase self-hosted service.

| | |
|---|---|
| **Image** | `ghcr.io/muchobien/pocketbase:latest` |
| **Host port** | `8090` |
| **Container port** | `8090` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | HTTP `/api/health` |

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
config/                   # mounted to /config
data/                     # mounted to /data
```

## Check it is healthy

```bash
docker inspect --format '{{.State.Health.Status}}' pocketbase
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
