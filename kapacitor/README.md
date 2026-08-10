# Kapacitor

Data process and monitoring application; TICK stack component

| | |
|---|---|
| **Image** | `kapacitor:latest` |
| **Host port** | `9092` |
| **Container port** | `9092` |
| **Category** | Analytics |
| **Healthcheck** | HTTP `/kapacitor/v1/ping` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:9092>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml kapacitor
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
docker inspect --format '{{.State.Health.Status}}' kapacitor
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
