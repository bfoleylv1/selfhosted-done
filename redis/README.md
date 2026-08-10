# Redis

In-memory key-value store; used as database, cache, and message broker.

| | |
|---|---|
| **Image** | `redis:7-alpine` |
| **Host port** | `20239` |
| **Container port** | `6379` |
| **Category** | Database Management |
| **Healthcheck** | TCP port probe |

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
config/                   # mounted to /config
data/                     # mounted to /data
```

## Check it is healthy

```bash
docker inspect --format '{{.State.Health.Status}}' redis
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
