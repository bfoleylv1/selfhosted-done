# Transmute

Transmute is an open-source file conversion and transformation service designed to handle a wide variety of document, media, and data format conversions through a clean API and web interface.

| | |
|---|---|
| **Image** | `ghcr.io/transmute-app/transmute:latest` |
| **Host port** | `3313` |
| **Container port** | `3313` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://localhost:3313/api/health/ready` |
| **Category** | File Sharing |
| **Upstream** | https://github.com/transmute-app/transmute |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:3313>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml transmute
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
