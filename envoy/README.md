# Envoy

High-performance proxy; service mesh and edge proxy solution.

| | |
|---|---|
| **Image** | `envoyproxy/envoy:v1.31-latest` |
| **Host port** | `10000` |
| **Container port** | `10000` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Api Management |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:10000>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml envoy
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
