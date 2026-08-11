# Awstats

Advanced web statistics; detailed reporting and log analysis.

| | |
|---|---|
| **Image** | `php:8.2-apache` |
| **Host port** | `20004` |
| **Container port** | `20004` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Analytics |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20004>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml awstats
```

## Layout

```
docker-compose.yml        # single-host deployment
swarm/docker-stack.yml    # swarm stack (named volumes, replicas, placement)
```

## Check it is healthy

```bash
docker compose ps
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
