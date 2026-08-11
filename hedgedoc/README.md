# Hedgedoc

Web-based markdown editor for collaborative note-taking.

| | |
|---|---|
| **Image** | `quay.io/hedgedoc/hedgedoc:latest` |
| **Host port** | `20111` |
| **Container port** | `3000` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:3000/` |
| **Category** | Productivity |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20111>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml hedgedoc
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
