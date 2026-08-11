# Makemkv

DVD/Blu-ray copying tool; extract video from optical discs.

| | |
|---|---|
| **Image** | `jlesage/makemkv:latest` |
| **Host port** | `20149` |
| **Container port** | `20149` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Media Conversion |
| **GPU** | hardware-acceleration block included (commented) |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20149>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml makemkv
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
