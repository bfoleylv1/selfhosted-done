# Kubernetes

System for automating deployment, scaling, and management.

| | |
|---|---|
| **Image** | `registry.k8s.io/kube-apiserver:v1.31.0` |
| **Host port** | `20135` |
| **Container port** | `8080` |
| **Category** | Automation |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20135>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml kubernetes
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
docker inspect --format '{{.State.Health.Status}}' kubernetes
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
