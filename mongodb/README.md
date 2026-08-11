# Mongodb

Document-oriented NoSQL database; stores JSON-like documents with flexible schemas.

| | |
|---|---|
| **Image** | `mongo:7` |
| **Host port** | `27017` |
| **Container port** | `27017` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Database Management |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:27017>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml mongodb
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
