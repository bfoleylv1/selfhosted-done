# DBeaver

Universal database tool; supports all major databases.

| | |
|---|---|
| **Image** | `dbeaver/cloudbeaver:latest` |
| **Host port** | `8978` |
| **Container port** | `8978` |
| **Category** | Database Tools |
| **Healthcheck** | HTTP `/` |

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
config/                   # mounted to /config
data/                     # mounted to /data
```

## Check it is healthy

```bash
docker inspect --format '{{.State.Health.Status}}' dbeaver
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
