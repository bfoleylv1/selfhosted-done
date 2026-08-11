# Newwallpaperwhodis

NewWallpaperWhoDis is a lightweight, self-hosted wallpaper manager designed to turn browsers, tablets, smart TVs, Raspberry Pis, dashboards, and other display endpoints into dynamic smart displays.

| | |
|---|---|
| **Image** | `ghcr.io/upioneer/newwallpaperwhodis:latest` |
| **Host port** | `20594` |
| **Container port** | `6767` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:3000/favicon.svg` |
| **Category** | Additional Services |
| **Upstream** | https://github.com/upioneer/NewWallpaperWhoDis |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20594>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml newwallpaperwhodis
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
