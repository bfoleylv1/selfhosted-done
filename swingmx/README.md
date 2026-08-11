# Swing Music

Swing Music is a fast, beautiful, self-hosted music player and streaming server for your local audio collection.

| | |
|---|---|
| **Image** | `ghcr.io/swingmx/swingmusic:latest` |
| **Host port** | `1970` |
| **Container port** | `1970` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Music |
| **Upstream** | https://github.com/swingmx/swingmusic |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:1970>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml swingmx
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
