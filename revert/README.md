# Revert

Placeholder entry — no real upstream image configured (generic base image only); not yet implemented

| | |
|---|---|
| **Image** | `node:20-alpine` |
| **Host port** | `20247` |
| **Container port** | `20247` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20247>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml revert
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
