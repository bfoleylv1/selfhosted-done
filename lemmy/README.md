# Lemmy

Decentralised link aggregation; Reddit-like topic browsing

| | |
|---|---|
| **Image** | `dessalines/lemmy:0.19.5` |
| **Host port** | `8536` |
| **Container port** | `8536` |
| **Category** | Social |
| **Healthcheck** | HTTP `/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:8536>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml lemmy
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
docker inspect --format '{{.State.Health.Status}}' lemmy
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
