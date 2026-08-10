# Druid

druid self-hosted service.

| | |
|---|---|
| **Image** | `apache/druid:31.0.0` |
| **Host port** | `20053` |
| **Container port** | `8888` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | HTTP `/status/health` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20053>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml druid
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
docker inspect --format '{{.State.Health.Status}}' druid
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
