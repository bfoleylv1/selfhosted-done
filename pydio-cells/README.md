# Pydio Cells

Enterprise file sharing and sync platform; modern alternative to Nextcloud.

| | |
|---|---|
| **Image** | `pydio/cells:latest` |
| **Host port** | `20226` |
| **Container port** | `8080` |
| **Category** | File |
| **Healthcheck** | HTTP `/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20226>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml pydio-cells
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
docker inspect --format '{{.State.Health.Status}}' pydio-cells
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
