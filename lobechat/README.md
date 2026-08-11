# Lobechat

LobeChat: open-source chatbot platform with multi-model support and plugin ecosystem

| | |
|---|---|
| **Image** | `lobehub/lobe-chat:latest` |
| **Host port** | `20469` |
| **Container port** | `20469` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20469>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml lobechat
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
