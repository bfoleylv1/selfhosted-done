# Wireguard Vpn

Fast modern VPN using the WireGuard protocol

| | |
|---|---|
| **Image** | `lscr.io/linuxserver/wireguard:latest` |
| **Host port** | `20366` |
| **Container port** | `51820` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20366>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml wireguard-vpn
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
docker inspect --format '{{.State.Health.Status}}' wireguard-vpn
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
