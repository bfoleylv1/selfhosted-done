# Configarr

Configarr is a configuration management tool designed to declaratively manage and synchronize settings for Radarr, Sonarr, and related media services.

| | |
|---|---|
| **Image** | `ghcr.io/raydak-labs/configarr:latest` |
| **Host port** | _none (headless)_ |
| **Container port** | _n/a_ |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Automation |
| **Upstream** | https://github.com/raydak-labs/configarr |

## Run it

Single host:

```bash
docker compose up -d
```

This service has no web UI; it runs headless.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml configarr
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
