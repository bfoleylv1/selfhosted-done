# Paperless-ngx

Paperless-ngx is a community-supported open-source document management system that transforms your physical documents into a searchable online archive so you can keep, well, less paper.

| | |
|---|---|
| **Image** | `ghcr.io/paperless-ngx/paperless-ngx:latest` |
| **Host port** | `20598` |
| **Container port** | `80` |
| **Containers** | 3 (app + db, broker) |
| **Healthcheck** | command probe |
| **Category** | Content Management Systems |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20598>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml paperless
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
