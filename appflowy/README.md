# Appflowy

Open source Notion alternative; collaborative workspace builder.

| | |
|---|---|
| **Image** | `appflowyinc/appflowy_cloud:latest` |
| **Host port** | `20002` |
| **Container port** | `80` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:80/` |
| **Category** | Productivity |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20002>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml appflowy
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
