# Tyk

Open source API gateway; full lifecycle API management.

| | |
|---|---|
| **Image** | `tykio/tyk-gateway:latest` |
| **Host port** | `20340` |
| **Container port** | `8080` |
| **Category** | Api Management |
| **Healthcheck** | HTTP `/hello` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20340>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml tyk
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
docker inspect --format '{{.State.Health.Status}}' tyk
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
