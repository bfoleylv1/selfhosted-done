# Neo4J

Graph database optimized for storing and querying relationships between data.

| | |
|---|---|
| **Image** | `neo4j:5` |
| **Host port** | `7474` |
| **Container port** | `7474` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Database Management |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:7474>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml neo4j
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
