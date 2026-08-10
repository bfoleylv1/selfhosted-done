# Element

Element: feature-rich web client for the Matrix decentralized chat protocol

| | |
|---|---|
| **Image** | `vectorim/element-web:latest` |
| **Host port** | `20438` |
| **Container port** | `20438` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20438>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml element
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
docker inspect --format '{.State.Health.Status}' element
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
