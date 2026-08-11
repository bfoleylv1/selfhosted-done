# Homepage

Homepage is a modern, customizable, and self-hosted dashboard for organizing and accessing your personal services and information.

| | |
|---|---|
| **Image** | `ghcr.io/gethomepage/homepage:latest` |
| **Host port** | `20582` |
| **Container port** | `3000` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |
| **Upstream** | https://github.com/gethomepage/homepage |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20582>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml homepage
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
