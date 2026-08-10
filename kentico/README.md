# Kentico

All-in-one CMS; e-commerce and online marketing platform.

| | |
|---|---|
| **Image** | `mcr.microsoft.com/dotnet/aspnet:8.0` |
| **Host port** | `20124` |
| **Container port** | `8080` |
| **Category** | Content Management Systems |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20124>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml kentico
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
docker inspect --format '{{.State.Health.Status}}' kentico
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
