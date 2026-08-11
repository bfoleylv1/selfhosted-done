# Hytale

The Hytale server runs from deinfreu/hytale-server:experimental and is configured for UDP port 5520.

| | |
|---|---|
| **Image** | `deinfreu/hytale-server:experimental` |
| **Host port** | `5520` |
| **Container port** | `5520` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:5520/` |
| **Category** | Additional Services |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:5520>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml hytale
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
