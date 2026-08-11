# Commentario

Self-hosted comment system for static sites

| | |
|---|---|
| **Image** | `registry.gitlab.com/comentario/comentario:latest` |
| **Host port** | `20036` |
| **Container port** | `20036` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20036>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml commentario
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
