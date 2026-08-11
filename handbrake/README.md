# Handbrake

Video transcoder; convert videos to optimized formats.

| | |
|---|---|
| **Image** | `linuxserver/handbrake:latest` |
| **Host port** | `5800` |
| **Container port** | `5800` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Media Conversion |
| **GPU** | hardware-acceleration block included (commented) |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:5800>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml handbrake
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
