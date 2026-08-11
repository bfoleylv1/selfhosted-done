# Openwebui

Self-hosted OpenAI-powered web UI; chat with AI models locally.

| | |
|---|---|
| **Image** | `ghcr.io/open-webui/open-webui:main` |
| **Host port** | `20184` |
| **Container port** | `8080` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:8080/` |
| **Category** | Analytics |
| **GPU** | hardware-acceleration block included (commented) |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20184>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml openwebui
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
