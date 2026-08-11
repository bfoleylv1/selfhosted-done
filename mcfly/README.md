# Mcfly

McFly is a smarter shell history search tool with a TUI (not a server app).

| | |
|---|---|
| **Image** | `segrettodozuki/mcfly:latest` |
| **Host port** | `20474` |
| **Container port** | `20474` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20474>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml mcfly
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
