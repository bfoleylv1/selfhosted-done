# Radarr

PVR for movie fans; manages and automatically downloads films.

| | |
|---|---|
| **Image** | `lscr.io/linuxserver/radarr:latest` |
| **Host port** | `20230` |
| **Container port** | `7878` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:7878/` |
| **Category** | Audio |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20230>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml radarr
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
