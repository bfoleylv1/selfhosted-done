# OSSEC

Host-based intrusion detection system; log analysis and monitoring.

| | |
|---|---|
| **Image** | `atomicorp/ossec-docker:latest` |
| **Host port** | `1514` |
| **Container port** | `1514` |
| **Category** | Security |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:1514>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml ossec
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
docker inspect --format '{{.State.Health.Status}}' ossec
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
