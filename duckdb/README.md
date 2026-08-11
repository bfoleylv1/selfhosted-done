# Duckdb

In-process SQL OLAP database similar to SQLite but for analytics.

| | |
|---|---|
| **Image** | `davidgasquez/duckdb:latest` |
| **Host port** | `20055` |
| **Container port** | `20055` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Database Management |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20055>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml duckdb
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
