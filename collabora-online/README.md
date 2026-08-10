# Collabora Online

Self-hosted LibreOffice-based online office suite

| | |
|---|---|
| **Image** | `collabora/code:latest` |
| **Host port** | `9980` |
| **Container port** | `9980` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | HTTP `/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:9980>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml collabora-online
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
docker inspect --format '{{.State.Health.Status}}' collabora-online
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
