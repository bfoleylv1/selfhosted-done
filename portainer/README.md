# Portainer

Lightweight web UI for managing Docker, Swarm and Kubernetes

| | |
|---|---|
| **Image** | `portainer/portainer-ce:latest` |
| **Host port** | `9443` |
| **Container port** | `9443` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:9443/api/health` |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:9443>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml portainer
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
