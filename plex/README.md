# Plex

Media server for organizing and streaming your media library.

| | |
|---|---|
| **Image** | `linuxserver/plex:latest` |
| **Host port** | `32400` |
| **Container port** | `32400` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:32400/web` |
| **Category** | Audio |
| **GPU** | hardware-acceleration block included (commented) |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:32400>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml plex
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
