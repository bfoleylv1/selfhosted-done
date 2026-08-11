# Nanote

Nanote is a lightweight, self-hosted note-taking application designed for simplicity and speed.

| | |
|---|---|
| **Image** | `omarmir/nanote:latest` |
| **Host port** | `20592` |
| **Container port** | `3000` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://localhost:3000/api/health` |
| **Category** | Productivity |
| **Upstream** | https://github.com/omarmir/nanote |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20592>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml nanote
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
