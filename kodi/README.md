# Kodi

Free and open source media center; entertainment system hub.

| | |
|---|---|
| **Image** | `lscr.io/linuxserver/webtop:ubuntu-kde` |
| **Host port** | `20131` |
| **Container port** | `8080` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:8080/` |
| **Category** | Video |
| **GPU** | hardware-acceleration block included (commented) |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20131>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml kodi
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
