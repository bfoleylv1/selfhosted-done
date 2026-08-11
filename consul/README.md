# Consul

Service mesh solution; service discovery and configuration.

| | |
|---|---|
| **Image** | `hashicorp/consul:latest` |
| **Host port** | `8500` |
| **Container port** | `8500` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:8500/v1/agent/health` |
| **Category** | Automation |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:8500>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml consul
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
