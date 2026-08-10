# Alfresco

Alfresco Community Edition: open-source enterprise content management (ECM) platform

| | |
|---|---|
| **Image** | `alfresco/alfresco-content-repository-community:latest` |
| **Host port** | `20408` |
| **Container port** | `20408` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20408>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml alfresco
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
docker inspect --format '{.State.Health.Status}' alfresco
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
