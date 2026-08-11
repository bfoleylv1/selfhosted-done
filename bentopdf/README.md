# BentoPDF

BentoPDF is an open-source, self-hosted web application for viewing, organizing, and managing PDF documents.

| | |
|---|---|
| **Image** | `ghcr.io/alam00000/bentopdf:latest` |
| **Host port** | `20560` |
| **Container port** | `3000` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:8080/` |
| **Category** | Productivity |
| **Upstream** | https://github.com/alam00000/bentopdf |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20560>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml bentopdf
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
