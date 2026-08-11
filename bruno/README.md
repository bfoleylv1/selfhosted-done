# Bruno

Self-hosted service: bruno.

| | |
|---|---|
| **Image** | `alpine/bruno:latest` |
| **Host port** | `20418` |
| **Container port** | `20418` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20418>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml bruno
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
