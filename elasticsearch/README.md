# Elasticsearch

Distributed search and analytics engine; scalable data store and vector database for production workloads.

| | |
|---|---|
| **Image** | `docker.elastic.co/elasticsearch/elasticsearch:8.15.0` |
| **Host port** | `9200` |
| **Container port** | `9200` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:9200/` |
| **Category** | Search Engines |
| **GPU** | hardware-acceleration block included (commented) |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:9200>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml elasticsearch
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
