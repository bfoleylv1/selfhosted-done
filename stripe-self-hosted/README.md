# Stripe Self Hosted

Self-hosted Stripe integration / API proxy

| | |
|---|---|
| **Image** | `node:20-alpine` |
| **Host port** | `20308` |
| **Container port** | `20308` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20308>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml stripe-self-hosted
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
