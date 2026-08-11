# Mailu

Open source email suite; complete mail server stack.

| | |
|---|---|
| **Image** | `ghcr.io/mailu/admin:2.0` |
| **Host port** | `20148` |
| **Container port** | `20148` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Email |

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
```

## Check it is healthy

```bash
docker compose ps
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
