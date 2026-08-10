# Tuwunel

Matrix homeserver written in Rust

| | |
|---|---|
| **Image** | `ghcr.io/matrix-construct/tuwunel:latest` |
| **Host port** | `20338` |
| **Container port** | `6167` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | HTTP `/_matrix/client/versions` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20338>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml tuwunel
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
docker inspect --format '{{.State.Health.Status}}' tuwunel
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
