# Algo Vpn

VPN servers; deploy IPsec VPN on popular cloud providers

| | |
|---|---|
| **Image** | `ubuntu:24.04` |
| **Host port** | `20401` |
| **Container port** | `20401` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Vpn |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20401>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml algo-vpn
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
