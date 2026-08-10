# Graylog

Open source log management platform; centralized log management.

| | |
|---|---|
| **Image** | `graylog/graylog:6.1` |
| **Host port** | `20106` |
| **Container port** | `9000` |
| **Category** | Security |
| **Healthcheck** | HTTP `/api` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20106>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml graylog
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
docker inspect --format '{{.State.Health.Status}}' graylog
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
