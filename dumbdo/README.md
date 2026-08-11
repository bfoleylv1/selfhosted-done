# Dumbdo

DumbDo is a self-hosted, minimalistic task management tool designed to provide a distraction-free experience for managing to-do lists and tasks.

| | |
|---|---|
| **Image** | `dumbwareio/dumbdo:latest` |
| **Host port** | `20571` |
| **Container port** | `3000` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:3000/` |
| **Category** | Productivity |
| **Upstream** | https://github.com/DumbWareio/DumbDo |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20571>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml dumbdo
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
