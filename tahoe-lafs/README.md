# Tahoe-LAFS

Decentralized, fault-tolerant, encrypted file storage grid.

| | |
|---|---|
| **Image** | `tahoelafs/base:latest` |
| **Host port** | `3456` |
| **Container port** | `3456` |
| **Category** | File |
| **Healthcheck** | TCP port probe |

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
config/                   # mounted to /config
data/                     # mounted to /data
```

## Check it is healthy

```bash
docker inspect --format '{{.State.Health.Status}}' tahoe-lafs
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
