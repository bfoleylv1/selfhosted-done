# Nginx Proxy Manager

Web interface for managing Nginx proxies; simple reverse proxy

| | |
|---|---|
| **Image** | `jc21/nginx-proxy-manager:latest` |
| **Host port** | `20167` |
| **Container port** | `20167` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Additional Services |

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
```

## Check it is healthy

```bash
docker compose ps
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
