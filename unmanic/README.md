# Unmanic

Self-hosted service: unmanic.

| | |
|---|---|
| **Image** | `josh5/unmanic:latest` |
| **Host port** | `20613` |
| **Container port** | `80` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Media Conversion |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20613>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml unmanic
```

## Configuration

Settings live in `.env` next to the compose file. Generated secrets are already filled in and are stable across regeneration.

## Layout

```
docker-compose.yml        # single-host deployment
swarm/docker-stack.yml    # swarm stack (named volumes, replicas, placement)
.env                      # configuration and generated secrets
```

## Check it is healthy

```bash
docker compose ps
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
