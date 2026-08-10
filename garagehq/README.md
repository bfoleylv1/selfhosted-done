# Garagehq

Lightweight S3-compatible distributed object storage

| | |
|---|---|
| **Image** | `dxflrs/garage:v1.0.1` |
| **Host port** | `3900` |
| **Container port** | `3900` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:3900>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml garagehq
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
docker inspect --format '{{.State.Health.Status}}' garagehq
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
