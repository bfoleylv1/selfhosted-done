# Datasette

Explore and publish SQLite databases as JSON APIs and dashboards

| | |
|---|---|
| **Image** | `datasetteproject/datasette:latest` |
| **Host port** | `8001` |
| **Container port** | `8001` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | HTTP `/-/versions.json` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:8001>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml datasette
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
docker inspect --format '{{.State.Health.Status}}' datasette
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
