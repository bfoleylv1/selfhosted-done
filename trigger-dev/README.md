# Trigger Dev

Open-source background jobs and workflow engine

| | |
|---|---|
| **Image** | `ghcr.io/triggerdotdev/trigger.dev:v3` |
| **Host port** | `20334` |
| **Container port** | `20334` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20334>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml trigger-dev
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
