# Miniflux

Simple and fast RSS reader; minimalist UI with excellent readability.

| | |
|---|---|
| **Image** | `miniflux/miniflux:latest` |
| **Host port** | `20156` |
| **Container port** | `8080` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:8080/healthcheck` |
| **Category** | Rss |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20156>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml miniflux
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
