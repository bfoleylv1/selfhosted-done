# Misskey

Microblogging platform forActivityPub; Japanese-originated.

| | |
|---|---|
| **Image** | `misskey/misskey:latest` |
| **Host port** | `20158` |
| **Container port** | `3000` |
| **Category** | Social |
| **Healthcheck** | HTTP `/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20158>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml misskey
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
docker inspect --format '{{.State.Health.Status}}' misskey
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
