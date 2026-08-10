# Librechat

LibreChat: open-source ChatGPT-compatible frontend with multi-model support and agents

| | |
|---|---|
| **Image** | `librechat/librechat:latest` |
| **Host port** | `20465` |
| **Container port** | `20465` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20465>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml librechat
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
docker inspect --format '{.State.Health.Status}' librechat
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
