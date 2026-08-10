# BookWyrm

Federated book social network; discover and discuss books.

| | |
|---|---|
| **Image** | `python:3.11-slim` |
| **Host port** | `8000` |
| **Container port** | `8000` |
| **Category** | Social |
| **Healthcheck** | HTTP `/` |

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
config/                   # mounted to /config
data/                     # mounted to /data
```

## Check it is healthy

```bash
docker inspect --format '{{.State.Health.Status}}' bookwyrm
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
