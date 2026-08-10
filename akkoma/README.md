# Akkoma

Lightweight federated microblogging server (ActivityPub, Mastodon-compatible)

| | |
|---|---|
| **Image** | `akkoma/akkoma:latest` |
| **Host port** | `20400` |
| **Container port** | `4000` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | HTTP `/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20400>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml akkoma
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
docker inspect --format '{{.State.Health.Status}}' akkoma
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
