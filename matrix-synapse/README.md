# Matrix Synapse

Decentralized communication protocol server; bridges to other services

| | |
|---|---|
| **Image** | `matrixdotorg/synapse:latest` |
| **Host port** | `8008` |
| **Container port** | `8008` |
| **Category** | Chat |
| **Healthcheck** | HTTP `/health` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:8008>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml matrix-synapse
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
docker inspect --format '{{.State.Health.Status}}' matrix-synapse
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
