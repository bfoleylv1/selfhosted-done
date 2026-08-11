# Posterizarr

Posterizarr is a companion tool for Radarr and Sonarr that automatically manages posters, backgrounds, and other artwork based on predefined rules.

| | |
|---|---|
| **Image** | `ghcr.io/fscorrupt/posterizarr:latest` |
| **Host port** | `20602` |
| **Container port** | `8000` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Media Conversion |
| **Upstream** | https://github.com/fscorrupt/Posterizarr |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20602>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml posterizarr
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
