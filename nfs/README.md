# Nfs

Network File System; share file systems on Unix/Linux.

| | |
|---|---|
| **Image** | `itsthenetwork/nfs-server-alpine:latest` |
| **Host port** | `2049` |
| **Container port** | `2049` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | File Sharing |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:2049>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml nfs
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
