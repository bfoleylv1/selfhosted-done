# Bookwyrm

Federated book social network; discover and discuss books.

| | |
|---|---|
| **Image** | `python:3.11-slim` |
| **Host port** | `8000` |
| **Container port** | `8000` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Social |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:8000>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml bookwyrm
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
