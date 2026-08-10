# FileBrowser

Web-based file manager with authentication; manages files and folders via browser

| | |
|---|---|
| **Image** | `filebrowser/filebrowser:latest` |
| **Host port** | `20069` |
| **Container port** | `80` |
| **Category** | File |
| **Healthcheck** | HTTP `/health` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20069>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml filebrowser
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
docker inspect --format '{{.State.Health.Status}}' filebrowser
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
