# Datasette

Explore and publish SQLite databases as JSON APIs and dashboards

| | |
|---|---|
| **Image** | `datasetteproject/datasette:latest` |
| **Host port** | `8001` |
| **Container port** | `8001` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

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
```

## Check it is healthy

```bash
docker compose ps
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
