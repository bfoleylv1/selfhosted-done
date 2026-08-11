# Navidrome

Modern and lightweight Go/NodeJS music server; compatible with Subsonic API.

| | |
|---|---|
| **Image** | `deluan/navidrome:latest` |
| **Host port** | `4533` |
| **Container port** | `4533` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:4533/` |
| **Category** | Music |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:4533>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml navidrome
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
