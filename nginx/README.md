# NGINX

Web server and reverse proxy; high-performance HTTP server.

| | |
|---|---|
| **Image** | `nginx:alpine` |
| **Host port** | `20166` |
| **Container port** | `80` |
| **Category** | Api Management |
| **Healthcheck** | HTTP `/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20166>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml nginx
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
docker inspect --format '{{.State.Health.Status}}' nginx
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
