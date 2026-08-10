# LinkAce

Link shortener and bookmark manager; save and share URLs.

| | |
|---|---|
| **Image** | `linkace/linkace:simple` |
| **Host port** | `20141` |
| **Container port** | `80` |
| **Category** | News |
| **Healthcheck** | HTTP `/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20141>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml linkace
```

## Layout

```
docker-compose.yml        # single-host deployment
swarm/docker-stack.yml    # swarm stack (named volumes, replicas, placement)
config/                   # mounted to /config
data/                     # mounted to /data
```

## Check it is healthy

```bash
docker inspect --format '{{.State.Health.Status}}' linkace
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
