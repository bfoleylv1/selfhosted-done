# Mailu

Open source email suite; complete mail server stack

| | |
|---|---|
| **Image** | `ghcr.io/mailu/admin:2.0` |
| **Host port** | `20148` |
| **Container port** | `80` |
| **Category** | Email |
| **Healthcheck** | HTTP `/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20148>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml mailu
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
docker inspect --format '{{.State.Health.Status}}' mailu
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
