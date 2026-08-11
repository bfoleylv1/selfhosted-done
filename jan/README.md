# Jan

Desktop app for running open-source models locally with GPU acceleration.

| | |
|---|---|
| **Image** | `python:3.11-slim` |
| **Host port** | `1337` |
| **Container port** | `1337` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:1337/` |
| **Category** | Ai |
| **GPU** | hardware-acceleration block included (commented) |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:1337>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml jan
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
