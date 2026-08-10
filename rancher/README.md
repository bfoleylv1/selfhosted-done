# Rancher

Container management platform; multi-cluster Kubernetes management.

| | |
|---|---|
| **Image** | `rancher/rancher:latest` |
| **Host port** | `20233` |
| **Container port** | `443` |
| **Category** | Automation |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20233>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml rancher
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
docker inspect --format '{{.State.Health.Status}}' rancher
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
