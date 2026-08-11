# Home Assistant

Home Assistant is an open-source home automation platform that allows you to control and automate smart devices from a unified interface.

| | |
|---|---|
| **Image** | `ghcr.io/home-assistant/home-assistant:stable` |
| **Host port** | `20581` |
| **Container port** | `8123` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://localhost:8123/` |
| **Category** | Automation |
| **Upstream** | https://github.com/home-assistant/ |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20581>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml home-assistant
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
