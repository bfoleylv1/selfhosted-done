# Tandoor

Tandoor Recipes is an application for managing recipes, planning meals, building shopping lists and much much more:

| | |
|---|---|
| **Image** | `vabene1111/recipes:latest` |
| **Host port** | `9001` |
| **Container port** | `9001` |
| **Containers** | 2 (app + database) |
| **Healthcheck** | command probe |
| **Category** | Additional Services |
| **Upstream** | https://github.com/TandoorRecipes/recipes |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:9001>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml tandoor
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
