# Prometheus

Monitoring and alerting toolkit; systems and services monitoring.

| | |
|---|---|
| **Image** | `prom/prometheus:latest` |
| **Host port** | `20221` |
| **Container port** | `9090` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:9090/-/healthy` |
| **Category** | Analytics |

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
```

## Check it is healthy

```bash
docker compose ps
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
