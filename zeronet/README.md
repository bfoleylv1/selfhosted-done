# Zeronet

Decentralized websites using Bitcoin crypto and BitTorrent swarm.

| | |
|---|---|
| **Image** | `nofish/zeronet:latest` |
| **Host port** | `20384` |
| **Container port** | `8080` |
| **Category** | Chat |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20384>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml zeronet
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
docker inspect --format '{{.State.Health.Status}}' zeronet
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
