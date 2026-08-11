# App

App is a generic self-hosted web application placeholder entry.

| | |
|---|---|
| **Image** | `istio/app:latest` |
| **Host port** | `20525` |
| **Container port** | `20525` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20525>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml app
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
