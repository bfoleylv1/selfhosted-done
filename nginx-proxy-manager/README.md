# NGINX Proxy Manager

Web interface for managing Nginx proxies; simple reverse proxy.

| | |
|---|---|
| **Image** | `jc21/nginx-proxy-manager:latest` |
| **Host port** | `20167` |
| **Container port** | `81` |
| **Category** | Additional Services |
| **Healthcheck** | HTTP `/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20167>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml nginx-proxy-manager
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
docker inspect --format '{{.State.Health.Status}}' nginx-proxy-manager
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
