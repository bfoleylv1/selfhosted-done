# Redis

In-memory key-value store; used as database, cache, and message broker.

| | |
|---|---|
| **Image** | `redis:7-alpine` |
| **Host port** | `20239` |
| **Container port** | `6379` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Database Management |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20239>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml redis
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
