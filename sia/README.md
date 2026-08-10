# Sia

Decentralized cloud storage; cryptocurrency-based storage

| | |
|---|---|
| **Image** | `ghcr.io/siafoundation/renterd:latest` |
| **Host port** | `20280` |
| **Container port** | `9980` |
| **Category** | Backup |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20280>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml sia
```

## Layout

```
docker-compose.yml        # single-host deployment
swarm/docker-stack.yml    # swarm stack (named volumes, replicas, placement)
config/                   # mounted to /config
data/                     # mounted to /data
```

## Check it is healthy

```bash
docker inspect --format '{{.State.Health.Status}}' sia
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
