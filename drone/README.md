# Drone

Continuous integration system; container-based CI/CD

| | |
|---|---|
| **Image** | `drone/drone:2` |
| **Host port** | `20052` |
| **Container port** | `80` |
| **Category** | Development |
| **Healthcheck** | HTTP `/healthz` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20052>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml drone
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
docker inspect --format '{{.State.Health.Status}}' drone
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
