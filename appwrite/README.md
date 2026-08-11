# Appwrite

Open-source backend-as-a-service (BaaS) for web and mobile apps

| | |
|---|---|
| **Image** | `appwrite/appwrite:1.6.0` |
| **Host port** | `20003` |
| **Container port** | `80` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:80/v1/health` |
| **Category** | Self Hosting Solutions |

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
```

## Check it is healthy

```bash
docker compose ps
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
