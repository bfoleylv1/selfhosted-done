# Tahoe Lafs

Decentralized, fault-tolerant, encrypted file storage grid

| | |
|---|---|
| **Image** | `tahoelafs/base:latest` |
| **Host port** | `3456` |
| **Container port** | `3456` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | File |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:3456>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml tahoe-lafs
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
