# Mesos

Distributed systems kernel; orchestrate containers and apps

| | |
|---|---|
| **Image** | `alpine:3.20` |
| **Host port** | `5050` |
| **Container port** | `5050` |
| **Category** | Monitoring |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:5050>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml mesos
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
docker inspect --format '{{.State.Health.Status}}' mesos
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
