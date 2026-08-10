# RowsHub

Collaborative spreadsheet platform; Airtable alternative.

| | |
|---|---|
| **Image** | `nocodb/nocodb:latest` |
| **Host port** | `20253` |
| **Container port** | `8080` |
| **Category** | Social |
| **Healthcheck** | HTTP `/api/health` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20253>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml rowshub
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
docker inspect --format '{{.State.Health.Status}}' rowshub
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
