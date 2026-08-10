# Joplin

Note-taking and to-do application; Markdown support with encryption

| | |
|---|---|
| **Image** | `joplin/server:latest` |
| **Host port** | `22300` |
| **Container port** | `22300` |
| **Category** | Productivity |
| **Healthcheck** | HTTP `/api/ping` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:22300>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml joplin
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
docker inspect --format '{{.State.Health.Status}}' joplin
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
