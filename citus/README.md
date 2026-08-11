# Citus

Extension to PostgreSQL; real-time analytics and scaling.

| | |
|---|---|
| **Image** | `citusdata/citus:12` |
| **Host port** | `20029` |
| **Container port** | `20029` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Database Tools |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20029>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml citus
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
