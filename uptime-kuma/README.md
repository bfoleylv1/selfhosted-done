# Uptime Kuma

Self-hosting status page; monitor websites and services

| | |
|---|---|
| **Image** | `louislam/uptime-kuma:1` |
| **Host port** | `20344` |
| **Container port** | `20344` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Additional Services |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20344>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml uptime-kuma
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
