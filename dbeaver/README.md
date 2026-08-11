# Dbeaver

Universal database tool; supports all major databases.

| | |
|---|---|
| **Image** | `dbeaver/cloudbeaver:latest` |
| **Host port** | `8978` |
| **Container port** | `8978` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:8978/` |
| **Category** | Database Tools |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:8978>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml dbeaver
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
