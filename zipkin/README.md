# Zipkin

Distributed tracing system; gather timing information.

| | |
|---|---|
| **Image** | `openzipkin/zipkin:latest` |
| **Host port** | `9411` |
| **Container port** | `9411` |
| **Category** | Monitoring |
| **Healthcheck** | HTTP `/health` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:9411>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml zipkin
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
docker inspect --format '{{.State.Health.Status}}' zipkin
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
