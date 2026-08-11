# Openshift

Kubernetes platform; enterprise container application platform.

| | |
|---|---|
| **Image** | `quay.io/openshift/origin-cli:latest` |
| **Host port** | `20181` |
| **Container port** | `20181` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Automation |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20181>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml openshift
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
