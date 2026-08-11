# Meilisearch

Lightning-fast search engine optimized for apps, websites, and workflows with relevant search experiences.

| | |
|---|---|
| **Image** | `getmeili/meilisearch:latest` |
| **Host port** | `7700` |
| **Container port** | `7700` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:7700/health` |
| **Category** | Search Engines |
| **GPU** | hardware-acceleration block included (commented) |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:7700>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml meilisearch
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
