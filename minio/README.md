# minIO

High-performance, distributed object storage; S3-compatible API.

| | |
|---|---|
| **Image** | `quay.io/minio/minio:latest` |
| **Host port** | `20157` |
| **Container port** | `9000` |
| **Category** | File |
| **Healthcheck** | HTTP `/minio/health/live` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20157>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml minio
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
docker inspect --format '{{.State.Health.Status}}' minio
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
