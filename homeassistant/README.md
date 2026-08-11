# Homeassistant

Home Assistant: open-source home automation platform

| | |
|---|---|
| **Image** | `ghcr.io/home-assistant/home-assistant:stable` |
| **Host port** | `20455` |
| **Container port** | `8123` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:8123/` |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20455>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml homeassistant
```

## Layout

```
docker-compose.yml        # single-host deployment
swarm/docker-stack.yml    # swarm stack (named volumes, replicas, placement)
```

## Check it is healthy

```bash
docker compose ps
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
