# Vllm

Fast library for LLM inference and serving; high-throughput inference engine.

| | |
|---|---|
| **Image** | `vllm/vllm-openai:latest` |
| **Host port** | `20351` |
| **Container port** | `8000` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:8000/health` |
| **Category** | Ai |
| **GPU** | hardware-acceleration block included (commented) |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20351>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml vllm
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
