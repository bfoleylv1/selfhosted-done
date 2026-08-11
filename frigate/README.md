# Frigate

AI-powered network video recorder (NVR) for camera streams

| | |
|---|---|
| **Image** | `ghcr.io/blakeblackshear/frigate:stable` |
| **Host port** | `20081` |
| **Container port** | `5000` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:5000/` |
| **Category** | Self Hosting Solutions |
| **GPU** | hardware-acceleration block included (commented) |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20081>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml frigate
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
