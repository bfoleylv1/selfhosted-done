# PlanetScale

Serverless MySQL platform; branchable databases.

| | |
|---|---|
| **Image** | `vitess/lite:latest` |
| **Host port** | `15000` |
| **Container port** | `15000` |
| **Category** | Database Tools |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:15000>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml planetscale
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
docker inspect --format '{{.State.Health.Status}}' planetscale
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
