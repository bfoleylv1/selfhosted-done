# Graphite

Enterprise monitoring and time-series database; monitoring graphs.

| | |
|---|---|
| **Image** | `graphiteapp/graphite-statsd:latest` |
| **Host port** | `20105` |
| **Container port** | `20105` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Analytics |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20105>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml graphite
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
