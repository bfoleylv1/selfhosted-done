# Cloudflare R2

S3-compatible object storage alternative to S3 with no egress fees

| | |
|---|---|
| **Image** | `minio/minio:latest` |
| **Host port** | `9000` |
| **Container port** | `9000` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | File |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:9000>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml cloudflare-r2
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
