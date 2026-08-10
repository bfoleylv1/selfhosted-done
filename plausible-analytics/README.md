# Plausible Analytics

Simple, privacy-focused web analytics alternative to Google Analytics.

| | |
|---|---|
| **Image** | `ghcr.io/plausible/community-edition:v2.1.4` |
| **Host port** | `20209` |
| **Container port** | `8000` |
| **Category** | Analytics |
| **Healthcheck** | HTTP `/api/health` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20209>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml plausible-analytics
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
docker inspect --format '{{.State.Health.Status}}' plausible-analytics
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
