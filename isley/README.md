# Isley

Isley is a self-hosted cannabis grow journal designed for home growers to track and monitor their plants with ease.

| | |
|---|---|
| **Image** | `dwot/isley:latest` |
| **Host port** | `20583` |
| **Container port** | `8080` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Additional Services |
| **Upstream** | https://github.com/dwot/isley |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20583>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml isley
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
