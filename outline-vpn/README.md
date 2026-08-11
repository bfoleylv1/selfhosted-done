# Outline Vpn

Secure team network access; Shadowsocks-based proxy

| | |
|---|---|
| **Image** | `quay.io/outline/shadowbox:stable` |
| **Host port** | `20187` |
| **Container port** | `20187` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Vpn |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20187>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml outline-vpn
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
