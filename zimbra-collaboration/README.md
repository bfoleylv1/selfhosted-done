# Zimbra Collaboration

Open-source email and collaboration suite

| | |
|---|---|
| **Image** | `ubuntu:24.04` |
| **Host port** | `20387` |
| **Container port** | `20387` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20387>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml zimbra-collaboration
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
