# BackupPC

High-performance clientless backup system; server and desktop backup.

| | |
|---|---|
| **Image** | `adferrand/backuppc:latest` |
| **Host port** | `20007` |
| **Container port** | `80` |
| **Category** | Backup |
| **Healthcheck** | HTTP `/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20007>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml backuppc
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
docker inspect --format '{{.State.Health.Status}}' backuppc
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
