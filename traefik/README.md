# Traefik

Modern reverse proxy; automatic service discovery and routing.

| | |
|---|---|
| **Image** | `traefik:v3.2` |
| **Host port** | `20332` |
| **Container port** | `80` |
| **Category** | Api Management |
| **Healthcheck** | TCP port probe |

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
config/                   # mounted to /config
data/                     # mounted to /data
```

## Check it is healthy

```bash
docker inspect --format '{{.State.Health.Status}}' traefik
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
