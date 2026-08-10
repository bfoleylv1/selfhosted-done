# Spree Commerce

Complete online store platform; Ruby on Rails based.

| | |
|---|---|
| **Image** | `ruby:3.3-alpine` |
| **Host port** | `20294` |
| **Container port** | `3000` |
| **Category** | Crm |
| **Healthcheck** | HTTP `/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20294>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml spree-commerce
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
docker inspect --format '{{.State.Health.Status}}' spree-commerce
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
