# Citus

Extension to PostgreSQL; real-time analytics and scaling.

| | |
|---|---|
| **Image** | `citusdata/citus:12` |
| **Host port** | `20029` |
| **Container port** | `5432` |
| **Category** | Database Tools |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20029>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml citus
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
docker inspect --format '{{.State.Health.Status}}' citus
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
