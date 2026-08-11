# Tempo

Distributed tracing platform; end-to-end telemetry collection.

| | |
|---|---|
| **Image** | `grafana/tempo:latest` |
| **Host port** | `3200` |
| **Container port** | `3200` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:3200/ready` |
| **Category** | Analytics |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:3200>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml tempo
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
