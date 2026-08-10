# HedgeDoc

Web-based markdown editor for collaborative note-taking.

| | |
|---|---|
| **Image** | `quay.io/hedgedoc/hedgedoc:latest` |
| **Host port** | `20111` |
| **Container port** | `3000` |
| **Category** | Productivity |
| **Healthcheck** | HTTP `/_health` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20111>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml hedgedoc
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
docker inspect --format '{{.State.Health.Status}}' hedgedoc
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
