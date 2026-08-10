# Authelia

Identity and Access Proxy providing 2FA, SSO, and access controls for services.

| | |
|---|---|
| **Image** | `authelia/authelia:latest` |
| **Host port** | `9091` |
| **Container port** | `9091` |
| **Category** | Authentication |
| **Healthcheck** | HTTP `/api/health` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:9091>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml authelia
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
docker inspect --format '{{.State.Health.Status}}' authelia
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
