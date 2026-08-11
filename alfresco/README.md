# Alfresco

Alfresco Community Edition: open-source enterprise content management (ECM) platform

| | |
|---|---|
| **Image** | `alfresco/alfresco-content-repository-community:latest` |
| **Host port** | `20408` |
| **Container port** | `20408` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

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
```

## Check it is healthy

```bash
docker compose ps
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
