# Plausible

Privacy-friendly, open-source web analytics

| | |
|---|---|
| **Image** | `ghcr.io/plausible/community-edition:v2.1.4` |
| **Host port** | `20208` |
| **Container port** | `8000` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | HTTP `/api/health` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20208>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml plausible
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
docker inspect --format '{{.State.Health.Status}}' plausible
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
