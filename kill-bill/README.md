# Kill Bill

Open source payment system; subscriptions and billing platform

| | |
|---|---|
| **Image** | `killbill/killbill:latest` |
| **Host port** | `20128` |
| **Container port** | `20128` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Payments |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20128>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml kill-bill
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
