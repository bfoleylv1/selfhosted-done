# Rocket.Chat

Web chat platform for teams; built with Meteor.js framework.

| | |
|---|---|
| **Image** | `registry.rocket.chat/rocketchat/rocket.chat:latest` |
| **Host port** | `20250` |
| **Container port** | `3000` |
| **Category** | Chat |
| **Healthcheck** | HTTP `/api/info` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20250>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml rocket-chat
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
docker inspect --format '{{.State.Health.Status}}' rocket-chat
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
