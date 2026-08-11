# Qdrant

Fast and privacy-friendly vector search engine with an easy-to-use gRPC API.

| | |
|---|---|
| **Image** | `qdrant/qdrant:latest` |
| **Host port** | `20227` |
| **Container port** | `6333` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:6333/` |
| **Category** | Search Engines |
| **GPU** | hardware-acceleration block included (commented) |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20227>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml qdrant
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
