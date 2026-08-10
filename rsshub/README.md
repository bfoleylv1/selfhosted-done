# RSSHub

Everything is an RSS feed; aggregates content from various sources to RSS

| | |
|---|---|
| **Image** | `diygod/rsshub:latest` |
| **Host port** | `1200` |
| **Container port** | `1200` |
| **Category** | Rss |
| **Healthcheck** | HTTP `/healthz` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:1200>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml rsshub
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
docker inspect --format '{{.State.Health.Status}}' rsshub
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
