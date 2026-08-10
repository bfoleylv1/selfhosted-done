# Formio

Form and API platform for building data-driven forms and apps

| | |
|---|---|
| **Image** | `formio/formio:latest` |
| **Host port** | `3001` |
| **Container port** | `3001` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | HTTP `/health` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:3001>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml formio
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
docker inspect --format '{{.State.Health.Status}}' formio
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
