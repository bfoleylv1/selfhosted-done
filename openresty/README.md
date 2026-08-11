# Openresty

NGINX with Lua; high-performance web platform.

| | |
|---|---|
| **Image** | `openresty/openresty:alpine` |
| **Host port** | `20179` |
| **Container port** | `20179` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Additional Services |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20179>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml openresty
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
