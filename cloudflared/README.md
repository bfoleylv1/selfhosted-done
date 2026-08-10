# Cloudflared

Cloudflare Tunnel; connect services without public IP.

| | |
|---|---|
| **Image** | `cloudflare/cloudflared:latest` |
| **Host port** | `20032` |
| **Container port** | `2000` |
| **Category** | Additional Services |
| **Healthcheck** | HTTP `/ready` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20032>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml cloudflared
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
docker inspect --format '{{.State.Health.Status}}' cloudflared
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
