# Roundcube

Web-based email client; webmail with plugins.

| | |
|---|---|
| **Image** | `roundcube/roundcubemail:latest` |
| **Host port** | `20251` |
| **Container port** | `80` |
| **Category** | Email |
| **Healthcheck** | HTTP `/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20251>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml roundcube
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
docker inspect --format '{{.State.Health.Status}}' roundcube
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
