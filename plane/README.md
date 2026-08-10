# Plane

Open source alternative to Notion and Linear; team project management.

| | |
|---|---|
| **Image** | `makeplane/plane-backend:latest` |
| **Host port** | `20207` |
| **Container port** | `80` |
| **Category** | Productivity |
| **Healthcheck** | HTTP `/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20207>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml plane
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
docker inspect --format '{{.State.Health.Status}}' plane
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
