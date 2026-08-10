# Appwrite

Open-source backend-as-a-service (BaaS) for web and mobile apps

| | |
|---|---|
| **Image** | `appwrite/appwrite:1.6.0` |
| **Host port** | `20003` |
| **Container port** | `80` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | HTTP `/v1/health` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20003>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml appwrite
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
docker inspect --format '{{.State.Health.Status}}' appwrite
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
