# Metabase

Metabase: open-source business intelligence and analytics dashboard tool

| | |
|---|---|
| **Image** | `metabase/metabase:latest` |
| **Host port** | `20553` |
| **Container port** | `3000` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:3000/api/health` |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20553>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml metabase
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
