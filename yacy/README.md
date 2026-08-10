# YaCy

Decentralized search engine; peer-to-peer indexing and search network.

| | |
|---|---|
| **Image** | `yacy/yacy_search_server:latest` |
| **Host port** | `20374` |
| **Container port** | `8090` |
| **Category** | Search Engines |
| **Healthcheck** | HTTP `/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20374>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml yacy
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
docker inspect --format '{{.State.Health.Status}}' yacy
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
