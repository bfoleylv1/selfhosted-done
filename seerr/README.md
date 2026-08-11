# Seerr

Seerr is an open-source request management and media discovery tool built to work with Plex, Jellyfin and Emby.

| | |
|---|---|
| **Image** | `ghcr.io/seerr-team/seerr:latest` |
| **Host port** | `5055` |
| **Container port** | `5055` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://localhost:5055/api/v1/status` |
| **Category** | Video |
| **Upstream** | https://github.com/seerr-team/seerr |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:5055>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml seerr
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
