# Flameborn

Open source media server; modern interface with advanced features.

| | |
|---|---|
| **Image** | `alpine:3.20` |
| **Host port** | `20070` |
| **Container port** | `8080` |
| **Category** | Audio |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20070>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml flameborn
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
docker inspect --format '{{.State.Health.Status}}' flameborn
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
