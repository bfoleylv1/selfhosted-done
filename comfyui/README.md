# Comfyui

Node-based graphical UI for Stable Diffusion / generative AI

| | |
|---|---|
| **Image** | `ghcr.io/ai-dock/comfyui:latest` |
| **Host port** | `8188` |
| **Container port** | `8188` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:8188/` |
| **Category** | Self Hosting Solutions |
| **GPU** | hardware-acceleration block included (commented) |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:8188>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml comfyui
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
