# Traefik

Modern reverse proxy; automatic service discovery and routing.

| | |
|---|---|
| **Image** | `traefik:v3.2` |
| **Host port** | `20332` |
| **Container port** | `8080` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:8080/ping` |
| **Category** | Api Management |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20332>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml traefik
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
