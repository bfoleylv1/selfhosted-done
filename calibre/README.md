# Calibre

Calibre: open-source e-book management and conversion server (Calibre-Web companion)

| | |
|---|---|
| **Image** | `linuxserver/calibre:latest` |
| **Host port** | `8083` |
| **Container port** | `8083` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:8083/` |
| **Category** | Self Hosting Solutions |

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
```

## Check it is healthy

```bash
docker compose ps
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
