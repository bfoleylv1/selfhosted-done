# Sentry (Self-Hosted)

Open-source error tracking tool; monitor and improve software

| | |
|---|---|
| **Image** | `sentry:latest` |
| **Host port** | `20272` |
| **Container port** | `9000` |
| **Category** | Analytics |
| **Healthcheck** | HTTP `/_health/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20272>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml sentry
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
docker inspect --format '{{.State.Health.Status}}' sentry
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
