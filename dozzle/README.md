# Dozzle

Dozzle is a lightweight, self-hosted application for viewing Docker container logs in real time.

| | |
|---|---|
| **Image** | `amir20/dozzle:latest` |
| **Host port** | `20570` |
| **Container port** | `8080` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Monitoring |
| **Upstream** | https://github.com/amir20/dozzle |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20570>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml dozzle
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
