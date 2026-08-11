# Influxdb

Time-series database optimized for metrics, events, and real-time analytics.

| | |
|---|---|
| **Image** | `influxdb:2` |
| **Host port** | `8086` |
| **Container port** | `8086` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:8086/health` |
| **Category** | Database Management |

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
```

## Check it is healthy

```bash
docker compose ps
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
