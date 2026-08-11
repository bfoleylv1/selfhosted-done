# Wallos

Wallos is a self-hosted subscription tracking application that helps you manage and visualize your recurring expenses.

| | |
|---|---|
| **Image** | `bellamy/wallos:latest` |
| **Host port** | `20615` |
| **Container port** | `80` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Additional Services |
| **Upstream** | https://github.com/ellite/Wallos |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20615>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml wallos
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
