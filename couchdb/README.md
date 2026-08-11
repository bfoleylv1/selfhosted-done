# Couchdb

ouchdb-style JSON document database with MVCC and multi-master replication

| | |
|---|---|
| **Image** | `couchdb:3` |
| **Host port** | `5984` |
| **Container port** | `5984` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Database Management |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:5984>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml couchdb
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
