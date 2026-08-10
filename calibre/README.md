# Calibre

Calibre: open-source e-book management and conversion server (Calibre-Web companion)

| | |
|---|---|
| **Image** | `linuxserver/calibre:latest` |
| **Host port** | `8083` |
| **Container port** | `8083` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:8083>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml calibre
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
docker inspect --format '{.State.Health.Status}' calibre
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
