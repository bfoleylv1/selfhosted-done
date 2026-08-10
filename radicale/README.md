# Radicale

Simple CalDAV and CardDAV server

| | |
|---|---|
| **Image** | `tomsquest/docker-radicale:latest` |
| **Host port** | `5232` |
| **Container port** | `5232` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | HTTP `/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:5232>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml radicale
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
docker inspect --format '{{.State.Health.Status}}' radicale
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
