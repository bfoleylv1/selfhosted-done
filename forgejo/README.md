# Forgejo

Fork of Gitea; community-driven Git service

| | |
|---|---|
| **Image** | `codeberg.org/forgejo/forgejo:9` |
| **Host port** | `20073` |
| **Container port** | `3000` |
| **Category** | Development |
| **Healthcheck** | HTTP `/api/healthz` |

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
config/                   # mounted to /config
data/                     # mounted to /data
```

## Check it is healthy

```bash
docker inspect --format '{{.State.Health.Status}}' forgejo
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
