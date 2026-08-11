# Flaresolverr

FlareSolverr is an open-source proxy server to bypass Cloudflare and other anti-bot protections.

| | |
|---|---|
| **Image** | `ghcr.io/flaresolverr/flaresolverr:latest` |
| **Host port** | `8191` |
| **Container port** | `8191` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:8191/` |
| **Category** | Network |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:8191>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml flaresolverr
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
