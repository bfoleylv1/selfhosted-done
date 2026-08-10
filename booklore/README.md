# Booklore

Self-hosted book library and reading tracker

| | |
|---|---|
| **Image** | `ghcr.io/booklore-app/booklore:latest` |
| **Host port** | `6060` |
| **Container port** | `6060` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | HTTP `/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:6060>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml booklore
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
docker inspect --format '{{.State.Health.Status}}' booklore
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
