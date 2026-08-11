# Zomboyin

Full-text search engine; JavaScript-based search.

| | |
|---|---|
| **Image** | `alpine:3.20` |
| **Host port** | `20389` |
| **Container port** | `20389` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Search Engines (Specialized) |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20389>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml zomboyin
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
