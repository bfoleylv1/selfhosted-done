# Libvirt

Open source virtualization API; manage VMs and containers.

| | |
|---|---|
| **Image** | `ubuntu:24.04` |
| **Host port** | `16509` |
| **Container port** | `16509` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Virtualization |
| **GPU** | hardware-acceleration block included (commented) |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:16509>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml libvirt
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
