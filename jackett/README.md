# Jackett

API for torrent indexers; acts as a bridge between downloaders and indexers.

| | |
|---|---|
| **Image** | `lscr.io/linuxserver/jackett:latest` |
| **Host port** | `9117` |
| **Container port** | `9117` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Audio |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:9117>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml jackett
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
