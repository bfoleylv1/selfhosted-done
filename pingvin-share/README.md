# Pingvin Share

Pingvin Share is a simple, open-source file-sharing application designed to make sharing files quick, easy, and efficient.

| | |
|---|---|
| **Image** | `stonith404/pingvin-share:latest` |
| **Host port** | `20601` |
| **Container port** | `3000` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | File Sharing |
| **Upstream** | https://github.com/stonith404/pingvin-share |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20601>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml pingvin-share
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
