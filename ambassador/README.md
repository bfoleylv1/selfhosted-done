# Ambassador

L7 load balancer; Kubernetes-native application delivery controller.

| | |
|---|---|
| **Image** | `docker.io/emissaryingress/emissary:3.9.1` |
| **Host port** | `20403` |
| **Container port** | `20403` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Api Management |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20403>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml ambassador
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
