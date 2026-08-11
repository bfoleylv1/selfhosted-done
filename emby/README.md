# Emby

Media system for organizing and streaming video, music, and photos.

| | |
|---|---|
| **Image** | `linuxserver/emby:latest` |
| **Host port** | `8096` |
| **Container port** | `8096` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:8096/health` |
| **Category** | Audio |
| **GPU** | hardware-acceleration block included (commented) |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:8096>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml emby
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
