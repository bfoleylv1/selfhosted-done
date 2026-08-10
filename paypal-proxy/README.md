# Paypal Proxy

paypal-proxy self-hosted service.

| | |
|---|---|
| **Image** | `node:20-alpine` |
| **Host port** | `20196` |
| **Container port** | `3000` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20196>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml paypal-proxy
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
docker inspect --format '{{.State.Health.Status}}' paypal-proxy
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
