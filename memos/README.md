# Memos

Self-hosted service: memos.

| | |
|---|---|
| **Image** | `neosmemo/memos:stable` |
| **Host port** | `5230` |
| **Container port** | `5230` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:5230/api/health` |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:5230>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml memos
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
