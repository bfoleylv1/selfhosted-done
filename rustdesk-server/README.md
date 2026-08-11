# RustDesk Server

Rustdesk Server information about the service.

| | |
|---|---|
| **Image** | `rustdesk/rustdesk-server:latest` |
| **Host port** | `20606` |
| **Container port** | `80` |
| **Containers** | 2 (app + hbbr) |
| **Healthcheck** | HTTP `http://127.0.0.1:80/` |
| **Category** | Network |
| **Upstream** | https://github.com/rustdesk/rustdesk/discussions/7118 |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20606>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml rustdesk-server
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
