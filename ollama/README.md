# Ollama

Get started with Llama, Gemma, and other language models locally.

| | |
|---|---|
| **Image** | `ollama/ollama:latest` |
| **Host port** | `11434` |
| **Container port** | `11434` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:11434/api/tags` |
| **Category** | Ai |
| **GPU** | hardware-acceleration block included (commented) |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:11434>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml ollama
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
