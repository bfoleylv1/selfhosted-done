# Ghostery

Privacy / tracker-blocking browser extension (commercial)

| | |
|---|---|
| **Image** | `alpine:3.20` |
| **Host port** | `20089` |
| **Container port** | `20089` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20089>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml ghostery
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
