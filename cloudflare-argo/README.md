# Cloudflare Argo

Cloudflare's smart routing; secure and fast connections

| | |
|---|---|
| **Image** | `cloudflare/cloudflared:latest` |
| **Host port** | `2000` |
| **Container port** | `2000` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Additional Services |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:2000>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml cloudflare-argo
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
