# Clipcascade

ClipCascade is a self-hosted, open-source clipboard manager that synchronizes and organizes clipboard history across devices.

| | |
|---|---|
| **Image** | `sathvikrao/clipcascade:latest` |
| **Host port** | `20562` |
| **Container port** | `8080` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Productivity |
| **Upstream** | https://github.com/Sathvik-Rao/ClipCascade |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20562>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml clipcascade
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
