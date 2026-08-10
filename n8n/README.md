# N8N

n8n: open-source workflow automation tool with 400+ integrations

| | |
|---|---|
| **Image** | `n8nio/n8n:latest` |
| **Host port** | `5678` |
| **Container port** | `5678` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | TCP port probe |

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
config/                   # mounted to /config
data/                     # mounted to /data
```

## Check it is healthy

```bash
docker inspect --format '{.State.Health.Status}' n8n
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
