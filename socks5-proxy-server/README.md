# Socks5 Proxy Server

socks5-proxy-server self-hosted service.

| | |
|---|---|
| **Image** | `serjs/go-socks5-proxy:latest` |
| **Host port** | `1080` |
| **Container port** | `1080` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:1080>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml socks5-proxy-server
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
docker inspect --format '{{.State.Health.Status}}' socks5-proxy-server
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
