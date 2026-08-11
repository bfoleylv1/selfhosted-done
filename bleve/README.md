# Bleve

Modern text search and analytics; Go full-text search library.

| | |
|---|---|
| **Image** | `golang:1.23-alpine` |
| **Host port** | `20015` |
| **Container port** | `20015` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Search Engines (Specialized) |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20015>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml bleve
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
