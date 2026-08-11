# Lidarr

PVR for music; automatically downloads and organizes music albums.

| | |
|---|---|
| **Image** | `lscr.io/linuxserver/lidarr:latest` |
| **Host port** | `8686` |
| **Container port** | `8686` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:8686/` |
| **Category** | Audio |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:8686>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml lidarr
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
