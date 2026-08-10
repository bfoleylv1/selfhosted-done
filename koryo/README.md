# Koryo

Simple API gateway; lightweight and fast reverse proxy

| | |
|---|---|
| **Image** | `alpine:3.20` |
| **Host port** | `20134` |
| **Container port** | `8080` |
| **Category** | Api Management |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20134>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml koryo
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
docker inspect --format '{{.State.Health.Status}}' koryo
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
