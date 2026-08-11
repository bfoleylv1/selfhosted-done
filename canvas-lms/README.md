# Canvas Lms

Open-source learning management system (LMS)

| | |
|---|---|
| **Image** | `instructure/canvas-lms:stable` |
| **Host port** | `3000` |
| **Container port** | `3000` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:3000>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml canvas-lms
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
