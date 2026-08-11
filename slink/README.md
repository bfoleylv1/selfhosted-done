# Slink

Slink is a fast, self-hosted alternative to ShareDrop, enabling secure, real-time file sharing over local networks.

| | |
|---|---|
| **Image** | `anirdev/slink:latest` |
| **Host port** | `20607` |
| **Container port** | `3000` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | File Sharing |
| **Upstream** | https://github.com/andrii-kryvoviaz/slink |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20607>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml slink
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
