# Convertx

ConvertX is a self-hosted, user-friendly media conversion tool designed to automate the process of converting media files using hardware acceleration where available.

| | |
|---|---|
| **Image** | `ghcr.io/c4illin/convertx:latest` |
| **Host port** | `20564` |
| **Container port** | `3000` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Media Conversion |
| **Upstream** | https://github.com/C4illin/ConvertX |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20564>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml convertx
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
