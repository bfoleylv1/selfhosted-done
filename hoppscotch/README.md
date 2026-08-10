# Hoppscotch

Hoppscotch Community Edition: open-source API development ecosystem (requests, testing, collaboration)

| | |
|---|---|
| **Image** | `hoppscotch/hoppscotch:latest` |
| **Host port** | `20456` |
| **Container port** | `20456` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20456>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml hoppscotch
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
docker inspect --format '{.State.Health.Status}' hoppscotch
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
