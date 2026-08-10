# Pocket (Self-Hosted Clone)

Save articles for later reading; privacy-focused alternative.

| | |
|---|---|
| **Image** | `alpine:3.20` |
| **Host port** | `20212` |
| **Container port** | `8080` |
| **Category** | News |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20212>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml pocket
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
docker inspect --format '{{.State.Health.Status}}' pocket
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
