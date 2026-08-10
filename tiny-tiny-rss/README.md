# Tiny Tiny RSS

Web-based news reader; customizable and extensible RSS aggregator

| | |
|---|---|
| **Image** | `php:8.2-fpm` |
| **Host port** | `20331` |
| **Container port** | `9000` |
| **Category** | Rss |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20331>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml tiny-tiny-rss
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
docker inspect --format '{{.State.Health.Status}}' tiny-tiny-rss
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
