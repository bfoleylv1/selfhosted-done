# DuckDB

In-process SQL OLAP database similar to SQLite but for analytics.

| | |
|---|---|
| **Image** | `davidgasquez/duckdb:latest` |
| **Host port** | `20055` |
| **Container port** | `8080` |
| **Category** | Database Management |
| **Healthcheck** | TCP port probe |

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
config/                   # mounted to /config
data/                     # mounted to /data
```

## Check it is healthy

```bash
docker inspect --format '{{.State.Health.Status}}' duckdb
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
