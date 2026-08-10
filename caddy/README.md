# Caddy

Easy to run HTTP web server; automatic HTTPS and simple configuration.

| | |
|---|---|
| **Image** | `caddy:alpine` |
| **Host port** | `20022` |
| **Container port** | `80` |
| **Category** | Api Management |
| **Healthcheck** | HTTP `/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20022>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml caddy
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
docker inspect --format '{{.State.Health.Status}}' caddy
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
