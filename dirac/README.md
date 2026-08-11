# Dirac

Dirac is a self-hosted media asset management system for video and broadcast workflows.

| | |
|---|---|
| **Image** | `zeppai/dirac:latest` |
| **Host port** | `20532` |
| **Container port** | `20532` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20532>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml dirac
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
