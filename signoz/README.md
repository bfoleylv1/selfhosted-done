# Signoz

Open-source observability platform (traces, metrics, logs)

| | |
|---|---|
| **Image** | `signoz/query-service:latest` |
| **Host port** | `20281` |
| **Container port** | `3301` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:3301/` |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20281>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml signoz
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
