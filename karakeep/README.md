# Karakeep

Self-hosted service: karakeep.

| | |
|---|---|
| **Image** | `ghcr.io/karakeep-app/karakeep:release` |
| **Host port** | `20461` |
| **Container port** | `3000` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:3000/api/health` |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20461>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml karakeep
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
