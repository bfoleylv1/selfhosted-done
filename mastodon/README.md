# Mastodon

Server for Twitter-like microblogging; federated social network

| | |
|---|---|
| **Image** | `ghcr.io/mastodon/mastodon:latest` |
| **Host port** | `20151` |
| **Container port** | `3000` |
| **Category** | Social |
| **Healthcheck** | HTTP `/health` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20151>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml mastodon
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
docker inspect --format '{{.State.Health.Status}}' mastodon
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
