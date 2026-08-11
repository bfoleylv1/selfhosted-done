# Kavita

Kavita is an open-source, self-hosted digital library manager optimized for comics, manga, and ebooks.

| | |
|---|---|
| **Image** | `jvmilazz0/kavita:latest` |
| **Host port** | `20586` |
| **Container port** | `5000` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Content Management Systems |
| **Upstream** | https://github.com/Kareadita/Kavita |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20586>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml kavita
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
