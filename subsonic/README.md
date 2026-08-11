# Subsonic

Web media streaming platform; the progenitor for many forks.

| | |
|---|---|
| **Image** | `lscr.io/linuxserver/airsonic-advanced:latest` |
| **Host port** | `4040` |
| **Container port** | `4040` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:4040/` |
| **Category** | Music |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:4040>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml subsonic
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
