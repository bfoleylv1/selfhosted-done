# Recast

Media server with transcoding; organize and watch your TV shows/movies.

| | |
|---|---|
| **Image** | `alpine:3.20` |
| **Host port** | `20237` |
| **Container port** | `20237` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Video |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20237>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml recast
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
