# Magento

Open-source e-commerce platform; Adobe Commerce predecessor.

| | |
|---|---|
| **Image** | `alexcheng/magento2:latest` |
| **Host port** | `20146` |
| **Container port** | `8080` |
| **Category** | Crm |
| **Healthcheck** | HTTP `/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20146>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml magento
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
docker inspect --format '{{.State.Health.Status}}' magento
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
