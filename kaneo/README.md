# Kaneo

Kaneo is an open-source, self-hosted project management platform focused on simplicity, clean UI, and efficient workflows.

| | |
|---|---|
| **Image** | `ghcr.io/usekaneo/web:latest` |
| **Host port** | `20585` |
| **Container port** | `5173` |
| **Containers** | 3 (app + postgres, backend) |
| **Healthcheck** | HTTP `http://127.0.0.1:5173/` |
| **Category** | Productivity |
| **Upstream** | https://github.com/usekaneo/kaneo |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20585>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml kaneo
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
