# Bifrost

Media server with Jellyfin-like features; open source and self-hosted.

| | |
|---|---|
| **Image** | `alpine:3.20` |
| **Host port** | `20012` |
| **Container port** | `8080` |
| **Category** | Audio |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20012>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml bifrost
```

## Layout

```
docker-compose.yml        # single-host deployment
swarm/docker-stack.yml    # swarm stack (named volumes, replicas, placement)
config/                   # mounted to /config
data/                     # mounted to /data
```

## Check it is healthy

```bash
docker inspect --format '{{.State.Health.Status}}' bifrost
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
