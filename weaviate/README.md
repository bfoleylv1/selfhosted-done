# Weaviate

GraphQL-native vector database with class-based object storage and search capabilities.

| | |
|---|---|
| **Image** | `semitechnologies/weaviate:latest` |
| **Host port** | `20358` |
| **Container port** | `8080` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:8080/v1/meta` |
| **Category** | Search Engines |
| **GPU** | hardware-acceleration block included (commented) |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20358>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml weaviate
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
