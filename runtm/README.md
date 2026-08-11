# Runtm

RunTM is a self-hosted tool for running and tracking timed tasks.

| | |
|---|---|
| **Image** | `(unset)` |
| **Host port** | `20546` |
| **Container port** | `20546` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20546>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml runtm
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
