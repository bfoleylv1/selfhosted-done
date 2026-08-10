# Library Genesis (Sci-Hub Mirror)

Digital library of books, articles, and academic papers

| | |
|---|---|
| **Image** | `nginx:alpine` |
| **Host port** | `20140` |
| **Container port** | `80` |
| **Category** | Search Engines |
| **Healthcheck** | HTTP `/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20140>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml library-genesis
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
docker inspect --format '{{.State.Health.Status}}' library-genesis
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
