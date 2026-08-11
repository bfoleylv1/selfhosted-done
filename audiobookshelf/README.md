# Audiobookshelf

Audiobookshelf is an open-source self-hosted application for managing and streaming audiobooks and podcasts.

| | |
|---|---|
| **Image** | `ghcr.io/advplyr/audiobookshelf:latest` |
| **Host port** | `20559` |
| **Container port** | `80` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Audio |
| **Upstream** | https://github.com/advplyr/audiobookshelf |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20559>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml audiobookshelf
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
