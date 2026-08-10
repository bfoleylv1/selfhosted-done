# OpenCart

Responsive e-commerce solution; ready-to-use online store platform.

| | |
|---|---|
| **Image** | `php:8.2-apache` |
| **Host port** | `20174` |
| **Container port** | `8080` |
| **Category** | Crm |
| **Healthcheck** | HTTP `/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20174>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml opencart
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
docker inspect --format '{{.State.Health.Status}}' opencart
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
