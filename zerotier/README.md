# ZeroTier

Smart networking platform; SD-WAN and SDN capabilities.

| | |
|---|---|
| **Image** | `zerotier/zerotier:latest` |
| **Host port** | `9993` |
| **Container port** | `9993` |
| **Category** | Vpn |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:9993>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml zerotier
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
docker inspect --format '{{.State.Health.Status}}' zerotier
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
