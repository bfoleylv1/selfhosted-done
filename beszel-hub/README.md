# Beszel Hub

The Beszel Hub is the core component responsible for routing messages between agents and managing the overall communication flow.

| | |
|---|---|
| **Image** | `henrygd/beszel:latest` |
| **Host port** | `20561` |
| **Container port** | `8090` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://localhost:8090` |
| **Category** | Monitoring |
| **Upstream** | https://github.com/henrygd/beszel |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20561>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml beszel-hub
```

## Configuration

Settings live in `.env` next to the compose file. Generated secrets are already filled in and are stable across regeneration.

## Layout

```
docker-compose.yml        # single-host deployment
swarm/docker-stack.yml    # swarm stack (named volumes, replicas, placement)
.env                      # configuration and generated secrets
```

## Check it is healthy

```bash
docker compose ps
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
