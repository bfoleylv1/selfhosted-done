# Enclosed

Self-hosted tool for sharing secrets and files securely

| | |
|---|---|
| **Image** | `ghcr.io/corentinth/enclosed:latest` |
| **Host port** | `8787` |
| **Container port** | `8787` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | HTTP `/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:8787>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml enclosed
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
docker inspect --format '{{.State.Health.Status}}' enclosed
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
