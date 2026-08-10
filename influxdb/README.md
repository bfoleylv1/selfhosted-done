# InfluxDB

Time-series database optimized for metrics, events, and real-time analytics

| | |
|---|---|
| **Image** | `influxdb:2` |
| **Host port** | `8086` |
| **Container port** | `8086` |
| **Category** | Database Management |
| **Healthcheck** | HTTP `/health` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:8086>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml influxdb
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
docker inspect --format '{{.State.Health.Status}}' influxdb
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
