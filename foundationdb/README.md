# Foundationdb

Ordered key-value database; transactions and scalability.

| | |
|---|---|
| **Image** | `foundationdb/foundationdb:7.3.27` |
| **Host port** | `4500` |
| **Container port** | `4500` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Database Tools |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:4500>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml foundationdb
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
