# Huginn

Huginn is a system for building agents that perform automated tasks and monitor the web.

| | |
|---|---|
| **Image** | `ghcr.io/huginn/huginn:latest` |
| **Host port** | `20552` |
| **Container port** | `20552` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20552>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml huginn
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
