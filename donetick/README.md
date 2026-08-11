# Donetick

Donetick is a self-hosted task and checklist manager designed for simplicity and efficiency.

| | |
|---|---|
| **Image** | `donetick/donetick:latest` |
| **Host port** | `2021` |
| **Container port** | `2021` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Productivity |
| **Upstream** | https://github.com/donetick/donetick |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:2021>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml donetick
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
