# Pinecone

Fully managed vector database alternative; private cloud deployment available

| | |
|---|---|
| **Image** | `qdrant/qdrant:latest` |
| **Host port** | `6333` |
| **Container port** | `6333` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Search Engines |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:6333>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml pinecone
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
