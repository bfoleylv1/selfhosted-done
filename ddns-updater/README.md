# Ddns Updater

DDNS Updater is a lightweight, universal program designed to keep your DNS A and/or AAAA records updated across multiple DNS providers.

| | |
|---|---|
| **Image** | `qmcgaw/ddns-updater:latest` |
| **Host port** | `20566` |
| **Container port** | `8000` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Network |
| **Upstream** | https://github.com/qdm12/ddns-updater |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20566>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml ddns-updater
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
