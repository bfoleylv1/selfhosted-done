# Espocrm

EspoCRM is a web application that allows users to see, enter and evaluate all your company relationships regardless of the type.

| | |
|---|---|
| **Image** | `espocrm/espocrm:latest` |
| **Host port** | `20573` |
| **Container port** | `80` |
| **Containers** | 2 (app + database) |
| **Healthcheck** | HTTP `http://127.0.0.1:80/` |
| **Category** | Crm |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20573>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml espocrm
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
