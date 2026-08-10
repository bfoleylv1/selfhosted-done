# Element Web App

Matrix client for secure decentralized communication

| | |
|---|---|
| **Image** | `vectorim/element-web:latest` |
| **Host port** | `20059` |
| **Container port** | `80` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | HTTP `/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20059>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml element-web-app
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
docker inspect --format '{{.State.Health.Status}}' element-web-app
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
