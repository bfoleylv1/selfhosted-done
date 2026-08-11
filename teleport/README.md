# Teleport

Teleport is an open-source access plane for SSH, Kubernetes and web apps with audit.

| | |
|---|---|
| **Image** | `public.ecr.aws/gravitational/teleport-distroless:16` |
| **Host port** | `20515` |
| **Container port** | `20515` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20515>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml teleport
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
