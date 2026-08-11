# Urbackup

Client/server backup solution; efficient backup and recovery.

| | |
|---|---|
| **Image** | `uroni/urbackup-server:latest` |
| **Host port** | `55414` |
| **Container port** | `55414` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Backup |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:55414>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml urbackup
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
