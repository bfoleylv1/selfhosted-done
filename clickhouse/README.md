# Clickhouse

Column-oriented database management system for OLAP and analytical workloads.

| | |
|---|---|
| **Image** | `clickhouse/clickhouse-server:latest` |
| **Host port** | `8123` |
| **Container port** | `8123` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:8123/ping` |
| **Category** | Database Management |
| **GPU** | hardware-acceleration block included (commented) |

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
```

## Check it is healthy

```bash
docker compose ps
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
