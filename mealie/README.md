# Mealie

Mealie is a self-hosted recipe management platform designed for home cooks, meal planners, and families.

| | |
|---|---|
| **Image** | `ghcr.io/mealie-recipes/mealie:latest` |
| **Host port** | `20590` |
| **Container port** | `9000` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:9000/` |
| **Category** | Additional Services |
| **Upstream** | https://github.com/mealie-recipes/mealie/ |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20590>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml mealie
```

## Configuration

Settings live in `.env` next to the compose file. Generated secrets are already filled in and are stable across regeneration.

## Layout

```
docker-compose.yml        # single-host deployment
swarm/docker-stack.yml    # swarm stack (named volumes, replicas, placement)
.env                      # configuration and generated secrets
```

## Check it is healthy

```bash
docker compose ps
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
