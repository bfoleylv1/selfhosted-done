# Resilio Sync

Resilio Sync is a powerful, peer-to-peer file synchronization tool that allows you to sync files between devices or share them with others, without relying on cloud services.

| | |
|---|---|
| **Image** | `linuxserver/resilio-sync:latest` |
| **Host port** | `20605` |
| **Container port** | `8888` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | File Sharing |
| **Upstream** | https://github.com/linuxserver/docker-resilio-sync |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20605>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml resilio-sync
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
