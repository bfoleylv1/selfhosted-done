# Ackee

Lightweight anonymised web analytics; self-hosted solution.

| | |
|---|---|
| **Image** | `electerious/ackee:latest` |
| **Host port** | `20394` |
| **Container port** | `3000` |
| **Category** | Analytics |
| **Healthcheck** | HTTP `/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20394>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml ackee
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
docker inspect --format '{{.State.Health.Status}}' ackee
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
