# Sonarr

PVR for TV shows; manages and automatically downloads series episodes.

| | |
|---|---|
| **Image** | `lscr.io/linuxserver/sonarr:latest` |
| **Host port** | `8989` |
| **Container port** | `8989` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:8989/` |
| **Category** | Audio |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:8989>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml sonarr
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
