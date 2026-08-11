# Formbricks

Formbricks is an open-source, self-hosted alternative to tools like Typeform, Hotjar, and Google Forms.

| | |
|---|---|
| **Image** | `ghcr.io/formbricks/formbricks:latest` |
| **Host port** | `20575` |
| **Container port** | `3000` |
| **Containers** | 3 (app + postgres, redis) |
| **Healthcheck** | HTTP `http://127.0.0.1:3000/` |
| **Category** | Analytics |
| **Upstream** | https://github.com/formbricks/formbricks |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20575>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml formbricks
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
