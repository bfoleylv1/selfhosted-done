# Kill Bill

Open source payment system; subscriptions and billing platform.

| | |
|---|---|
| **Image** | `killbill/killbill:latest` |
| **Host port** | `20128` |
| **Container port** | `8080` |
| **Category** | Payments |
| **Healthcheck** | HTTP `/1.0/healthcheck` |

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
config/                   # mounted to /config
data/                     # mounted to /data
```

## Check it is healthy

```bash
docker inspect --format '{{.State.Health.Status}}' kill-bill
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
