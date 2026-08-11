# Plume

Federation-friendly blogging platform; ActivityPub enabled.

| | |
|---|---|
| **Image** | `plumeorg/plume:latest` |
| **Host port** | `7878` |
| **Container port** | `7878` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Social |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:7878>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml plume
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
