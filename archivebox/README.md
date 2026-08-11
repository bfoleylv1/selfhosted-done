# Archivebox

ArchiveBox: open-source self-hosted internet archive (saves snapshots of websites)

| | |
|---|---|
| **Image** | `ghcr.io/archivebox/archivebox:latest` |
| **Host port** | `20413` |
| **Container port** | `8000` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:8000/` |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20413>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml archivebox
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
