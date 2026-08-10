# Glance

Self-hosted dashboard for your homelab and services

| | |
|---|---|
| **Image** | `glanceapp/glance:latest` |
| **Host port** | `20094` |
| **Container port** | `8080` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | HTTP `/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20094>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml glance
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
docker inspect --format '{{.State.Health.Status}}' glance
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
