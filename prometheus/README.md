# Prometheus

Monitoring and alerting toolkit; systems and services monitoring.

| | |
|---|---|
| **Image** | `prom/prometheus:latest` |
| **Host port** | `20221` |
| **Container port** | `9090` |
| **Category** | Analytics |
| **Healthcheck** | HTTP `/-/healthy` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20221>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml prometheus
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
docker inspect --format '{{.State.Health.Status}}' prometheus
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
