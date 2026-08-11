# Conduit

Lightweight Matrix homeserver written in Rust

| | |
|---|---|
| **Image** | `matrixconduit/matrix-conduit:latest` |
| **Host port** | `6167` |
| **Container port** | `6167` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:6167>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml conduit
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
