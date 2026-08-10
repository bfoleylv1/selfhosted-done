# Adyen Proxy

Reverse proxy / bridge for the Adyen payment API

| | |
|---|---|
| **Image** | `node:20-alpine` |
| **Host port** | `20396` |
| **Container port** | `3000` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20396>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml adyen-proxy
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
docker inspect --format '{{.State.Health.Status}}' adyen-proxy
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
