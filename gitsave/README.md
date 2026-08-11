# Gitsave

GitSave is a self-hosted tool for automatically backing up your GitHub repositories.

| | |
|---|---|
| **Image** | `timwitzdam/gitsave:latest` |
| **Host port** | `20577` |
| **Container port** | `3000` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Backup |
| **Upstream** | https://github.com/TimWitzdam/GitSave |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20577>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml gitsave
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
