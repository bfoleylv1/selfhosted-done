# Zerotier

Smart networking platform; SD-WAN and SDN capabilities.

| | |
|---|---|
| **Image** | `zerotier/zerotier:latest` |
| **Host port** | `9993` |
| **Container port** | `9993` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Vpn |

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
```

## Check it is healthy

```bash
docker compose ps
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
