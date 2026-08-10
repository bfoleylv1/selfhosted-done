# Notion Clone

Open-source Notion alternative for note-taking

| | |
|---|---|
| **Image** | `appflowyinc/appflowy_cloud:latest` |
| **Host port** | `20170` |
| **Container port** | `8000` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20170>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml notion-clone
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
docker inspect --format '{{.State.Health.Status}}' notion-clone
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
