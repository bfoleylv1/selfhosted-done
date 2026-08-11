# Docmost

Docmost is an open-source, self-hosted wiki and documentation tool designed for teams that want real-time collaboration without vendor lock-in.

| | |
|---|---|
| **Image** | `docmost/docmost:latest` |
| **Host port** | `20569` |
| **Container port** | `3000` |
| **Containers** | 3 (app + db, redis) |
| **Healthcheck** | command probe |
| **Category** | Content Management Systems |
| **Upstream** | https://github.com/docmost/docmost |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20569>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml docmost
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
