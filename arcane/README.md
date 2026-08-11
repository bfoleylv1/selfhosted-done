# Arcane

Arcane is an open-source, self-hosted platform for Docker container and Compose stack management with a modern web interface.

| | |
|---|---|
| **Image** | `ghcr.io/getarcaneapp/arcane:latest` |
| **Host port** | `3552` |
| **Container port** | `3552` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://localhost:3552/` |
| **Category** | Monitoring |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:3552>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml arcane
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
