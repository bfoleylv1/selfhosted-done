# Medusa

Alternative to Sonarr; PVR for TV shows with extensive customization.

| | |
|---|---|
| **Image** | `lscr.io/linuxserver/medusa:latest` |
| **Host port** | `8081` |
| **Container port** | `9000` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:9000/health` |
| **Category** | Audio |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:8081>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml medusa
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
