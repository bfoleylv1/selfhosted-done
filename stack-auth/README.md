# Stack Auth

Open-source authentication and user management

| | |
|---|---|
| **Image** | `node:20-alpine` |
| **Host port** | `20298` |
| **Container port** | `20298` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20298>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml stack-auth
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
