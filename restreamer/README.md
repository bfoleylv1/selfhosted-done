# Restreamer

Live video streaming server (RTSP/RTMP restreaming)

| | |
|---|---|
| **Image** | `datarhei/restreamer:latest` |
| **Host port** | `20244` |
| **Container port** | `20244` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |
| **GPU** | hardware-acceleration block included (commented) |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20244>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml restreamer
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
