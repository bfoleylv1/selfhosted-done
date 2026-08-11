# Plausible

Privacy-friendly, open-source web analytics

| | |
|---|---|
| **Image** | `ghcr.io/plausible/community-edition:v2.1.4` |
| **Host port** | `20208` |
| **Container port** | `8000` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:8000/api/health` |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20208>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml plausible
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
