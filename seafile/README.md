# Seafile

Professional file sync and share solution; focuses on efficiency and privacy.

| | |
|---|---|
| **Image** | `seafileltd/seafile-mc:latest` |
| **Host port** | `20266` |
| **Container port** | `8000` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:8000/` |
| **Category** | File |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20266>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml seafile
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
