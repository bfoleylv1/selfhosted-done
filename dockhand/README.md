# Dockhand

Dockhand is a modern, lightweight Docker management UI focused on real-time container operations and multi-environment orchestration.

| | |
|---|---|
| **Image** | `fnsys/dockhand:latest` |
| **Host port** | `20568` |
| **Container port** | `3000` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:41234/healthz` |
| **Category** | Monitoring |
| **Upstream** | https://github.com/Finsys/dockhand |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20568>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml dockhand
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
