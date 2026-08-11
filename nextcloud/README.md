# Nextcloud

Suite of client-server software for file syncing, collaboration, and video conferencing.

| | |
|---|---|
| **Image** | `nextcloud:stable` |
| **Host port** | `20165` |
| **Container port** | `80` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:80/` |
| **Category** | File |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20165>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml nextcloud
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
