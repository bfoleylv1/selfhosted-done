# Minio

High-performance object storage; S3-compatible.

| | |
|---|---|
| **Image** | `quay.io/minio/minio:latest` |
| **Host port** | `20157` |
| **Container port** | `9000` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:9000/minio/health/live` |
| **Category** | File |

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
```

## Check it is healthy

```bash
docker compose ps
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
