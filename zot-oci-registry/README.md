# Zot Oci Registry

OCI container image registry (Zot)

| | |
|---|---|
| **Image** | `ghcr.io/project-zot/zot-linux-amd64:latest` |
| **Host port** | `20390` |
| **Container port** | `20390` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20390>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml zot-oci-registry
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
