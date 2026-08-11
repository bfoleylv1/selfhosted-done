# Anythingllm

AnythingLLM: all-in-one desktop and self-hosted app for chatting with documents using LLMs

| | |
|---|---|
| **Image** | `mintplexlabs/anythingllm:latest` |
| **Host port** | `20412` |
| **Container port** | `3001` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:3001/api/health` |
| **Category** | Self Hosting Solutions |
| **GPU** | hardware-acceleration block included (commented) |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20412>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml anythingllm
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
