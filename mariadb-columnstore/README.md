# Mariadb Columnstore

Columnar storage engine for MariaDB; optimized for analytics workloads

| | |
|---|---|
| **Image** | `mariadb/columnstore:latest` |
| **Host port** | `20150` |
| **Container port** | `20150` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Database Management |

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
```

## Check it is healthy

```bash
docker compose ps
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
