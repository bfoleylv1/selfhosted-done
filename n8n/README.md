# N8N

n8n: open-source workflow automation tool with 400+ integrations

| | |
|---|---|
| **Image** | `n8nio/n8n:latest` |
| **Host port** | `5678` |
| **Container port** | `5678` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:5678/` |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:5678>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml n8n
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
