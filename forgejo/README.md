# Forgejo

Fork of Gitea; community-driven Git service.

| | |
|---|---|
| **Image** | `codeberg.org/forgejo/forgejo:9` |
| **Host port** | `20073` |
| **Container port** | `3000` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:3000/` |
| **Category** | Development |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20073>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml forgejo
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
