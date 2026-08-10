# Vaultwarden (Bitwarden RS)

Lightweight password manager server; Open Source Bitwarden implementation.

| | |
|---|---|
| **Image** | `vaultwarden/server:latest` |
| **Host port** | `20347` |
| **Container port** | `80` |
| **Category** | Authentication |
| **Healthcheck** | HTTP `/alive` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20347>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml vaultwarden
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
docker inspect --format '{{.State.Health.Status}}' vaultwarden
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
