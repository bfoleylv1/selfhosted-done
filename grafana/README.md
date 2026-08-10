# Grafana

Analytics and monitoring visualization platform; Grafana dashboards

| | |
|---|---|
| **Image** | `grafana/grafana:latest` |
| **Host port** | `20104` |
| **Container port** | `3000` |
| **Category** | Analytics |
| **Healthcheck** | HTTP `/api/health` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20104>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml grafana
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
docker inspect --format '{{.State.Health.Status}}' grafana
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
