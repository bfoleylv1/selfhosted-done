# Grampsweb

Gramps Web is an open-source, self-hosted web application for collaborative browsing and editing of genealogical data.

| | |
|---|---|
| **Image** | `ghcr.io/gramps-project/grampsweb:latest` |
| **Host port** | `20578` |
| **Container port** | `5000` |
| **Containers** | 3 (app + grampsweb_celery, grampsweb_redis) |
| **Healthcheck** | HTTP `http://127.0.0.1:5000/` |
| **Category** | Additional Services |
| **Upstream** | https://github.com/gramps-project/gramps-web |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20578>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml grampsweb
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
