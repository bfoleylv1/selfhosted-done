# Whoogle

Google search proxy; minimal Google search in your own server.

| | |
|---|---|
| **Image** | `benbusby/whoogle-search:latest` |
| **Host port** | `20362` |
| **Container port** | `5000` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:5000/` |
| **Category** | Search Engines |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20362>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml whoogle
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
