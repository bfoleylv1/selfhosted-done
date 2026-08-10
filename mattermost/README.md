# Mattermost

Open source Slack alternative; self-hosted team chat platform

| | |
|---|---|
| **Image** | `mattermost/mattermost-team-edition:latest` |
| **Host port** | `8065` |
| **Container port** | `8065` |
| **Category** | Chat |
| **Healthcheck** | HTTP `/api/v4/system/ping` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:8065>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml mattermost
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
docker inspect --format '{{.State.Health.Status}}' mattermost
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
