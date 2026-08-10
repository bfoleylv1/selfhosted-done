# Archivebox

ArchiveBox: open-source self-hosted internet archive (saves snapshots of websites)

| | |
|---|---|
| **Image** | `ghcr.io/archivebox/archivebox:latest` |
| **Host port** | `20413` |
| **Container port** | `20413` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | TCP port probe |

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
config/                   # mounted to /config
data/                     # mounted to /data
```

## Check it is healthy

```bash
docker inspect --format '{.State.Health.Status}' archivebox
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
