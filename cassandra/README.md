# Cassandra

Highly scalable NoSQL database; column-family store designed for large datasets.

| | |
|---|---|
| **Image** | `cassandra:5` |
| **Host port** | `9042` |
| **Container port** | `9042` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Database Management |

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
```

## Check it is healthy

```bash
docker compose ps
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
