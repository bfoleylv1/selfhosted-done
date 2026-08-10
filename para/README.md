# Para

Flexible open-source backend framework / object storage

| | |
|---|---|
| **Image** | `eclipse-temurin:17-jre` |
| **Host port** | `20190` |
| **Container port** | `8080` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | HTTP `/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20190>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml para
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
docker inspect --format '{{.State.Health.Status}}' para
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
