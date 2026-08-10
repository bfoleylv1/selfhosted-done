# CockroachDB

Cloud-native relational database; distributed SQL database

| | |
|---|---|
| **Image** | `cockroachdb/cockroach:latest` |
| **Host port** | `20035` |
| **Container port** | `8080` |
| **Category** | Database Tools |
| **Healthcheck** | HTTP `/health` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20035>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml cockroachdb
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
docker inspect --format '{{.State.Health.Status}}' cockroachdb
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
