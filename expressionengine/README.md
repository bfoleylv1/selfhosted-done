# ExpressionEngine

Flexible CMS; simple yet powerful content management

| | |
|---|---|
| **Image** | `php:8.2-apache` |
| **Host port** | `20066` |
| **Container port** | `80` |
| **Category** | Content Management Systems |
| **Healthcheck** | HTTP `/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20066>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml expressionengine
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
docker inspect --format '{{.State.Health.Status}}' expressionengine
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
