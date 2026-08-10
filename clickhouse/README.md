# ClickHouse

Column-oriented database management system for OLAP and analytical workloads.

| | |
|---|---|
| **Image** | `clickhouse/clickhouse-server:latest` |
| **Host port** | `8123` |
| **Container port** | `8123` |
| **Category** | Database Management |
| **Healthcheck** | HTTP `/ping` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:8123>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml clickhouse
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
docker inspect --format '{{.State.Health.Status}}' clickhouse
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
