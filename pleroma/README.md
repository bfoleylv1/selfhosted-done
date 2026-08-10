# Pleroma

Lightweight federated social network; alternative to Mastodon

| | |
|---|---|
| **Image** | `elixir:1.16-alpine` |
| **Host port** | `20210` |
| **Container port** | `4000` |
| **Category** | Social |
| **Healthcheck** | HTTP `/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20210>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml pleroma
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
docker inspect --format '{{.State.Health.Status}}' pleroma
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
