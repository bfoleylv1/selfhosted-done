# Synapse

Reference Matrix homeserver for federated chat

| | |
|---|---|
| **Image** | `matrixdotorg/synapse:latest` |
| **Host port** | `20318` |
| **Container port** | `8008` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:8008/health` |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20318>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml synapse
```

## Layout

```
docker-compose.yml        # single-host deployment
swarm/docker-stack.yml    # swarm stack (named volumes, replicas, placement)
```

## Check it is healthy

```bash
docker compose ps
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
