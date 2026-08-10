# Mimir

Grafana's long-term storage for Prometheus; scalable metrics.

| | |
|---|---|
| **Image** | `grafana/mimir:latest` |
| **Host port** | `20155` |
| **Container port** | `8080` |
| **Category** | Monitoring |
| **Healthcheck** | HTTP `/ready` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20155>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml mimir
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
docker inspect --format '{{.State.Health.Status}}' mimir
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
