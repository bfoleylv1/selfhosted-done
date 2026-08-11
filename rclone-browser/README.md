# Rclone Browser

GUI for Rclone; manage cloud storage with local file browser interface

| | |
|---|---|
| **Image** | `rclone/rclone:latest` |
| **Host port** | `20234` |
| **Container port** | `20234` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | File |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20234>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml rclone-browser
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
