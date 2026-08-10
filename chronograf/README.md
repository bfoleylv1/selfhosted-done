# Chronograf

Admin UI for InfluxDB; manage databases and monitoring

| | |
|---|---|
| **Image** | `chronograf:latest` |
| **Host port** | `20028` |
| **Container port** | `8888` |
| **Category** | Analytics |
| **Healthcheck** | HTTP `/ping` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20028>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml chronograf
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
docker inspect --format '{{.State.Health.Status}}' chronograf
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
