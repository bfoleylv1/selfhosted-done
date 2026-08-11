# Gokapi

Gokapi is a lightweight, self-hosted file-sharing platform designed to provide a simple and secure way to share files with others.

| | |
|---|---|
| **Image** | `f0rc3/gokapi:latest` |
| **Host port** | `53842` |
| **Container port** | `53842` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | File Sharing |
| **Upstream** | https://github.com/Forceu/Gokapi |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:53842>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml gokapi
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
