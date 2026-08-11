# Rsshub

Everything is an RSS feed; aggregates content from various sources to RSS.

| | |
|---|---|
| **Image** | `diygod/rsshub:latest` |
| **Host port** | `1200` |
| **Container port** | `1200` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:1200/` |
| **Category** | Rss |

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
```

## Check it is healthy

```bash
docker compose ps
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
