# Tempo

Distributed tracing platform; end-to-end telemetry collection

| | |
|---|---|
| **Image** | `grafana/tempo:latest` |
| **Host port** | `3200` |
| **Container port** | `3200` |
| **Category** | Analytics |
| **Healthcheck** | HTTP `/ready` |

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
config/                   # mounted to /config
data/                     # mounted to /data
```

## Check it is healthy

```bash
docker inspect --format '{{.State.Health.Status}}' tempo
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
