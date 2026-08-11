# Django Wiki

Self-hosted service: django-wiki.

| | |
|---|---|
| **Image** | `python:3.12-slim` |
| **Host port** | `20437` |
| **Container port** | `20437` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20437>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml django-wiki
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
