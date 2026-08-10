# Snipe-IT

Asset management solution; manage your IT assets and equipment

| | |
|---|---|
| **Image** | `snipe/snipe-it:latest` |
| **Host port** | `20286` |
| **Container port** | `80` |
| **Category** | Crm |
| **Healthcheck** | HTTP `/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20286>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml snipe-it
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
docker inspect --format '{{.State.Health.Status}}' snipe-it
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
