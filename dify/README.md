# Dify

Dify: open-source LLM app development platform (agents, RAG, workflows)

| | |
|---|---|
| **Image** | `langgenius/dify-api:latest` |
| **Host port** | `20531` |
| **Container port** | `20531` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20531>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml dify
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
docker inspect --format '{.State.Health.Status}' dify
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
