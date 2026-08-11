# Gpt4All

Software and models for running LLMs on consumer devices.

| | |
|---|---|
| **Image** | `python:3.11-slim` |
| **Host port** | `20103` |
| **Container port** | `8080` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:8080/` |
| **Category** | Ai |
| **GPU** | hardware-acceleration block included (commented) |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20103>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml gpt4all
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
