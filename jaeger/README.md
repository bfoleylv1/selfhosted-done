# Jaeger

Distributed tracing; monitoring microservices performance

| | |
|---|---|
| **Image** | `jaegertracing/all-in-one:latest` |
| **Host port** | `16686` |
| **Container port** | `16686` |
| **Category** | Monitoring |
| **Healthcheck** | HTTP `/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:16686>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml jaeger
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
docker inspect --format '{{.State.Health.Status}}' jaeger
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
