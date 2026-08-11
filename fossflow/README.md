# Fossflow

FossFLOW is a free and open-source flow visualization tool.

| | |
|---|---|
| **Image** | `stnsmith/fossflow:latest` |
| **Host port** | `20576` |
| **Container port** | `3000` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:3000` |
| **Category** | Productivity |
| **Upstream** | https://github.com/stan-smith/FossFLOW |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20576>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml fossflow
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
