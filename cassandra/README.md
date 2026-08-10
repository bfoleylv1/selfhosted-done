# Cassandra

Highly scalable NoSQL database; column-family store designed for large datasets

| | |
|---|---|
| **Image** | `cassandra:5` |
| **Host port** | `9042` |
| **Container port** | `9042` |
| **Category** | Database Management |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:9042>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml cassandra
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
docker inspect --format '{{.State.Health.Status}}' cassandra
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
