# Kitchenowl

Kitchenowl is a self-hosted grocery list, recipe manager, and meal planning application designed for households and shared kitchens.

| | |
|---|---|
| **Image** | `tombursch/kitchenowl:latest` |
| **Host port** | `20587` |
| **Container port** | `8080` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:8080/` |
| **Category** | Additional Services |
| **Upstream** | https://github.com/TomBursch/kitchenowl |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20587>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml kitchenowl
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
