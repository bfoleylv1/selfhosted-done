# Koboldai

UI for running language models; originally for GPT novels.

| | |
|---|---|
| **Image** | `koboldai/koboldai:latest` |
| **Host port** | `20130` |
| **Container port** | `5001` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:5001/` |
| **Category** | Ai |
| **GPU** | hardware-acceleration block included (commented) |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20130>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml koboldai
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
