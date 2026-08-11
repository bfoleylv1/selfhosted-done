# Eigenfocus

Eigenfocus is a self-hosted, privacy-focused task and project management tool that helps individuals and teams stay organized.

| | |
|---|---|
| **Image** | `eigenfocus/eigenfocus:0.8.0` |
| **Host port** | `20572` |
| **Container port** | `3000` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:3000/` |
| **Category** | Productivity |
| **Upstream** | https://github.com/Eigenfocus/eigenfocus |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20572>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml eigenfocus
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
