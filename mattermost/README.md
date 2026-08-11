# Mattermost

Open source Slack alternative; self-hosted team chat platform.

| | |
|---|---|
| **Image** | `mattermost/mattermost-team-edition:latest` |
| **Host port** | `8065` |
| **Container port** | `8065` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:8065/api/v4/system/ping` |
| **Category** | Chat |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:8065>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml mattermost
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
