# Loki

Log aggregation system; designed to be cost-effective and easily run.

| | |
|---|---|
| **Image** | `grafana/loki:latest` |
| **Host port** | `3100` |
| **Container port** | `3100` |
| **Category** | Analytics |
| **Healthcheck** | HTTP `/ready` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:3100>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml loki
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
docker inspect --format '{{.State.Health.Status}}' loki
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
