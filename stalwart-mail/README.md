# Stalwart Mail

stalwart-mail self-hosted service.

| | |
|---|---|
| **Image** | `stalwartlabs/stalwart:latest` |
| **Host port** | `20299` |
| **Container port** | `8080` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | HTTP `/healthz` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20299>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml stalwart-mail
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
docker inspect --format '{{.State.Health.Status}}' stalwart-mail
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
