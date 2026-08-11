# Streama

Self-hosted Netflix clone; organize and stream your media collection.

| | |
|---|---|
| **Image** | `eclipse-temurin:17-jre` |
| **Host port** | `20304` |
| **Container port** | `20304` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Audio |
| **GPU** | hardware-acceleration block included (commented) |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20304>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml streama
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
