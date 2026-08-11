# Kiwix

Offline Wikipedia reader; hosts ZIM file format for offline browsing.

| | |
|---|---|
| **Image** | `ghcr.io/kiwix/kiwix-serve:latest` |
| **Host port** | `20129` |
| **Container port** | `20129` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Search Engines |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20129>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml kiwix
```

## Layout

```
docker-compose.yml        # single-host deployment
swarm/docker-stack.yml    # swarm stack (named volumes, replicas, placement)
```

## Check it is healthy

```bash
docker compose ps
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
