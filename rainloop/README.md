# RainLoop

Webmail client; simple and responsive webmail

| | |
|---|---|
| **Image** | `hardware/rainloop:latest` |
| **Host port** | `20232` |
| **Container port** | `8888` |
| **Category** | Email |
| **Healthcheck** | HTTP `/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20232>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml rainloop
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
docker inspect --format '{{.State.Health.Status}}' rainloop
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
