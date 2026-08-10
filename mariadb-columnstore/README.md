# MariaDB ColumnStore

Columnar storage engine for MariaDB; optimized for analytics workloads

| | |
|---|---|
| **Image** | `mariadb/columnstore:latest` |
| **Host port** | `20150` |
| **Container port** | `3306` |
| **Category** | Database Management |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20150>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml mariadb-columnstore
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
docker inspect --format '{{.State.Health.Status}}' mariadb-columnstore
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
