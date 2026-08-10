# Spoolman

Filament and spool inventory manager for 3D printing

| | |
|---|---|
| **Image** | `ghcr.io/donkie/spoolman:latest` |
| **Host port** | `20293` |
| **Container port** | `8000` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | HTTP `/api/v1/health` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20293>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml spoolman
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
docker inspect --format '{{.State.Health.Status}}' spoolman
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
