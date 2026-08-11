# Paypal Proxy

Proxy for the PayPal payment API

| | |
|---|---|
| **Image** | `node:20-alpine` |
| **Host port** | `20196` |
| **Container port** | `20196` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20196>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml paypal-proxy
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
