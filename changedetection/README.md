# Changedetection

changedetection.io: self-hosted website change monitoring and notification service

| | |
|---|---|
| **Image** | `dgtlmoon/changedetection.io:latest` |
| **Host port** | `20422` |
| **Container port** | `20422` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20422>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml changedetection
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
docker inspect --format '{.State.Health.Status}' changedetection
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
