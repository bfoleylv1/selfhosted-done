# Kubernetes

System for automating deployment, scaling, and management.

| | |
|---|---|
| **Image** | `registry.k8s.io/kube-apiserver:v1.31.0` |
| **Host port** | `20135` |
| **Container port** | `6443` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:6443/healthz` |
| **Category** | Automation |
| **GPU** | hardware-acceleration block included (commented) |

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
```

## Check it is healthy

```bash
docker compose ps
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
