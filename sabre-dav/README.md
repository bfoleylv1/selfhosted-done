# Sabre Dav

WebDAV, CalDAV and CardDAV server library/framework

| | |
|---|---|
| **Image** | `php:8.2-apache` |
| **Host port** | `20260` |
| **Container port** | `20260` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20260>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml sabre-dav
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
