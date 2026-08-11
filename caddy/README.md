# Caddy

Easy to run HTTP web server; automatic HTTPS and simple configuration.

| | |
|---|---|
| **Image** | `caddy:alpine` |
| **Host port** | `20022` |
| **Container port** | `80` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:80/` |
| **Category** | Api Management |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20022>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml caddy
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
