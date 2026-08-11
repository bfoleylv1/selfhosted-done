# Sub Converter

Subtitle file converter; convert between different subtitle formats

| | |
|---|---|
| **Image** | `python:3.11-slim` |
| **Host port** | `25500` |
| **Container port** | `25500` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Media Conversion |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:25500>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml sub-converter
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
