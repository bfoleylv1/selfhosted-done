# Nginx

Web server and reverse proxy; high-performance HTTP server.

| | |
|---|---|
| **Image** | `nginx:alpine` |
| **Host port** | `20166` |
| **Container port** | `80` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:80/` |
| **Category** | Api Management |

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
```

## Check it is healthy

```bash
docker compose ps
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
