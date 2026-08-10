# Svix

Open-source webhook service and infrastructure

| | |
|---|---|
| **Image** | `svix/svix-server:latest` |
| **Host port** | `8071` |
| **Container port** | `8071` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | HTTP `/api/v1/health/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:8071>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml svix
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
docker inspect --format '{{.State.Health.Status}}' svix
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
