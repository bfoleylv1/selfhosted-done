# Victoriametrics

Ultra-high performing time series database; Prometheus compatible.

| | |
|---|---|
| **Image** | `victoriametrics/victoria-metrics:latest` |
| **Host port** | `8428` |
| **Container port** | `8428` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:8428/health` |
| **Category** | Monitoring |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:8428>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml victoriametrics
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
