# Homarr

Homarr is an open-source, self-hosted dashboard that integrates with all your self-hosted services, providing a centralized location to manage and access your apps, notifications, and more.

| | |
|---|---|
| **Image** | `ghcr.io/homarr-labs/homarr:latest` |
| **Host port** | `7575` |
| **Container port** | `7575` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |
| **Upstream** | https://github.com/ajnart/homarr |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:7575>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml homarr
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
