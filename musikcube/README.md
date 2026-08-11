# Musikcube

musikcube is a cross-platform, terminal-based music player and streaming server.

| | |
|---|---|
| **Image** | `hectormolinero/musikcube:latest` |
| **Host port** | `20480` |
| **Container port** | `20480` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20480>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml musikcube
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
