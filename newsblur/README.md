# NewsBlur

News reader with smart filtering; self-hosted version for news aggregation.

| | |
|---|---|
| **Image** | `python:3.11-slim` |
| **Host port** | `20163` |
| **Container port** | `8000` |
| **Category** | Rss |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20163>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml newsblur
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
docker inspect --format '{{.State.Health.Status}}' newsblur
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
