# TimescaleDB

PostgreSQL extension for time-series data; SQL for time-series

| | |
|---|---|
| **Image** | `timescale/timescaledb:latest-pg16` |
| **Host port** | `20329` |
| **Container port** | `5432` |
| **Category** | Database Tools |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20329>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml timescaledb
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
docker inspect --format '{{.State.Health.Status}}' timescaledb
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
