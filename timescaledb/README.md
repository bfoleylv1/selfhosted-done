# Timescaledb

PostgreSQL extension for time-series data; SQL for time-series.

| | |
|---|---|
| **Image** | `timescale/timescaledb:latest-pg16` |
| **Host port** | `20329` |
| **Container port** | `20329` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Database Tools |

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
```

## Check it is healthy

```bash
docker compose ps
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
