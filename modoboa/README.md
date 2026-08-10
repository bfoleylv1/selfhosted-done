# Modoboa

Mail hosting application; complete mail server suite.

| | |
|---|---|
| **Image** | `python:3.11-slim` |
| **Host port** | `20159` |
| **Container port** | `80` |
| **Category** | Email |
| **Healthcheck** | HTTP `/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20159>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml modoboa
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
docker inspect --format '{{.State.Health.Status}}' modoboa
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
