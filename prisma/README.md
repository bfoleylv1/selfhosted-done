# Prisma

Database toolkit; type-safe ORM with migrations

| | |
|---|---|
| **Image** | `node:20-alpine` |
| **Host port** | `5555` |
| **Container port** | `5555` |
| **Category** | Database Tools |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:5555>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml prisma
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
docker inspect --format '{{.State.Health.Status}}' prisma
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
