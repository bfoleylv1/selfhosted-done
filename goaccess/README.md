# Goaccess

Real-time web log analyzer; interactive HTML reports.

| | |
|---|---|
| **Image** | `allinurl/goaccess:latest` |
| **Host port** | `7890` |
| **Container port** | `7890` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Analytics |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:7890>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml goaccess
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
