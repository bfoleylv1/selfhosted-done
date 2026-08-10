# Adminer

Tool for managing MySQL, PostgreSQL, SQLite, and other databases.

| | |
|---|---|
| **Image** | `adminer:latest` |
| **Host port** | `20402` |
| **Container port** | `8080` |
| **Category** | Database Tools |
| **Healthcheck** | HTTP `/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20402>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml adminer
```

## Layout

```
docker-compose.yml        # single-host deployment
swarm/docker-stack.yml    # swarm stack (named volumes, replicas, placement)
config/                   # mounted to /config
data/                     # mounted to /data
```

## Check it is healthy

```bash
docker inspect --format '{{.State.Health.Status}}' adminer
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
