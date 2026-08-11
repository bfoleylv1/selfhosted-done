# Semantic Scholar

AI-powered research tool; academic paper search

| | |
|---|---|
| **Image** | `python:3.11-slim` |
| **Host port** | `20269` |
| **Container port** | `20269` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | News |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20269>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml semantic-scholar
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
