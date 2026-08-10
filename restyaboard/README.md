# Restyaboard

Open source Trello alternative; project management and task board

| | |
|---|---|
| **Image** | `php:8.2-apache` |
| **Host port** | `20245` |
| **Container port** | `8080` |
| **Category** | Productivity |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20245>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml restyaboard
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
docker inspect --format '{{.State.Health.Status}}' restyaboard
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
