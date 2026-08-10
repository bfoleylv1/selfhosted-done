# OpenVPN

SSL VPN solution; secure networking and remote access

| | |
|---|---|
| **Image** | `kylemanna/openvpn:latest` |
| **Host port** | `1194` |
| **Container port** | `1194` |
| **Category** | Vpn |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:1194>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml openvpn
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
docker inspect --format '{{.State.Health.Status}}' openvpn
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
