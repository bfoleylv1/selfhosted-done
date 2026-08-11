# Langflow

Langflow: visual builder for LangChain and LLM workflows

| | |
|---|---|
| **Image** | `langflowai/langflow:latest` |
| **Host port** | `20463` |
| **Container port** | `7860` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:7860/` |
| **Category** | Self Hosting Solutions |
| **GPU** | hardware-acceleration block included (commented) |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20463>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml langflow
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
