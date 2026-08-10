# Ghost

Publishing platform; focused on publishing and journalism

| | |
|---|---|
| **Image** | `ghost:5-alpine` |
| **Host port** | `2368` |
| **Container port** | `2368` |
| **Category** | Content Management Systems |
| **Healthcheck** | HTTP `/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:2368>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml ghost
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
docker inspect --format '{{.State.Health.Status}}' ghost
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
