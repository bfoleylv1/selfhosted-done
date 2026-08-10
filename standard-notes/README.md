# Standard Notes

Encrypted notes app; focus on privacy and security.

| | |
|---|---|
| **Image** | `standardnotes/server:latest` |
| **Host port** | `20300` |
| **Container port** | `3000` |
| **Category** | Productivity |
| **Healthcheck** | HTTP `/healthcheck` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20300>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml standard-notes
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
docker inspect --format '{{.State.Health.Status}}' standard-notes
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
