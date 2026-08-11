# Health Checker

Simple monitoring tool; check service availability

| | |
|---|---|
| **Image** | `lscr.io/linuxserver/healthchecks:latest` |
| **Host port** | `20110` |
| **Container port** | `20110` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Additional Services |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20110>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml health-checker
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
