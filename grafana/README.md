# Grafana

Analytics and monitoring visualization platform; Grafana dashboards.

| | |
|---|---|
| **Image** | `grafana/grafana:latest` |
| **Host port** | `20104` |
| **Container port** | `3000` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:3000/api/health` |
| **Category** | Analytics |

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
```

## Check it is healthy

```bash
docker compose ps
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
