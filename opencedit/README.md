# Opencedit

OpenCut is a self-hosted, open-source video editing platform.

| | |
|---|---|
| **Image** | `(unset)` |
| **Host port** | `20487` |
| **Container port** | `20487` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20487>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml opencedit
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
