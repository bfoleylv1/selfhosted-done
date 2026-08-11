# Reader Rise

Self-hosted Feedbin alternative; clean UI with OPML import/export

| | |
|---|---|
| **Image** | `alpine:3.20` |
| **Host port** | `20236` |
| **Container port** | `20236` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Rss |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20236>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml reader-rise
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
