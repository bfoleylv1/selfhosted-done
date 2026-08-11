# Vespa

Feature-rich search and ML engine; big data serving platform.

| | |
|---|---|
| **Image** | `vespaengine/vespa:latest` |
| **Host port** | `20349` |
| **Container port** | `20349` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Search Engines (Specialized) |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20349>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml vespa
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
