# Wireguard

Next-generation VPN protocol; fast and modern VPN solution.

| | |
|---|---|
| **Image** | `lscr.io/linuxserver/wireguard:latest` |
| **Host port** | `51820` |
| **Container port** | `51820` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Vpn |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:51820>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml wireguard
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
