# Pyload

pyLoad: lightweight, open-source download manager with a web interface (supports many one-click hosters)

| | |
|---|---|
| **Image** | `linuxserver/pyload:latest` |
| **Host port** | `20497` |
| **Container port** | `20497` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20497>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml pyload
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
