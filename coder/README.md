# Coder

Coder is an open-source, self-hosted platform that allows developers to define, provision, and secure web-based IDE workspaces (e.g., code-server, Jupyter) on cloud or local infrastructure.

| | |
|---|---|
| **Image** | `ghcr.io/coder/coder:latest` |
| **Host port** | `7080` |
| **Container port** | `7080` |
| **Containers** | 2 (app + database) |
| **Healthcheck** | command probe |
| **Category** | Development |
| **Upstream** | https://github.com/coder/coder |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:7080>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml coder
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
