# Solr

Enterprise search platform built on Apache Lucene; powerful full-text search capabilities.

| | |
|---|---|
| **Image** | `solr:9` |
| **Host port** | `8983` |
| **Container port** | `8983` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:8983/solr/` |
| **Category** | Search Engines |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:8983>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml solr
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
