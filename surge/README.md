# Surge

Placeholder entry — no real upstream image configured (generic base image only); not yet implemented

| | |
|---|---|
| **Image** | `node:20-alpine` |
| **Host port** | `20314` |
| **Container port** | `20314` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20314>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml surge
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
