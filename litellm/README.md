# Litellm

Proxy gateway for 100+ LLM providers with load balancing and fallbacks

| | |
|---|---|
| **Image** | `ghcr.io/berriai/litellm:main-latest` |
| **Host port** | `4000` |
| **Container port** | `4000` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:4000/health/liveliness` |
| **Category** | Self Hosting Solutions |
| **GPU** | hardware-acceleration block included (commented) |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:4000>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml litellm
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
