# Societies

Social login provider; bridges social accounts with local accounts

| | |
|---|---|
| **Image** | `alpine:3.20` |
| **Host port** | `20289` |
| **Container port** | `8080` |
| **Category** | Authentication |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20289>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml societies
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
docker inspect --format '{{.State.Health.Status}}' societies
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
