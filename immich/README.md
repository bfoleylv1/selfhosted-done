# Immich

Immich: self-hosted photo and video backup solution with AI search

| | |
|---|---|
| **Image** | `ghcr.io/immich-app/immich-server:release` |
| **Host port** | `2283` |
| **Container port** | `2283` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:2283/` |
| **Category** | Self Hosting Solutions |
| **GPU** | hardware-acceleration block included (commented) |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:2283>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml immich
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
