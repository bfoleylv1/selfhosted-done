# Thanos

Highly available Prometheus; long-term storage solution.

| | |
|---|---|
| **Image** | `quay.io/thanos/thanos:v0.37.2` |
| **Host port** | `10902` |
| **Container port** | `10901` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:10901/metrics` |
| **Category** | Monitoring |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:10902>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml thanos
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
