# MongoDB

Document-oriented NoSQL database; stores JSON-like documents with flexible schemas

| | |
|---|---|
| **Image** | `mongo:7` |
| **Host port** | `27017` |
| **Container port** | `27017` |
| **Category** | Database Management |
| **Healthcheck** | TCP port probe |

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
config/                   # mounted to /config
data/                     # mounted to /data
```

## Check it is healthy

```bash
docker inspect --format '{{.State.Health.Status}}' mongodb
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
