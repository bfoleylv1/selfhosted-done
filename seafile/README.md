# Seafile

Professional file sync and share solution; focuses on efficiency and privacy.

| | |
|---|---|
| **Image** | `seafileltd/seafile-mc:latest` |
| **Host port** | `20266` |
| **Container port** | `80` |
| **Category** | File |
| **Healthcheck** | HTTP `/` |

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
config/                   # mounted to /config
data/                     # mounted to /data
```

## Check it is healthy

```bash
docker inspect --format '{{.State.Health.Status}}' seafile
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
