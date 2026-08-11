# Kvm

Full virtualization for Linux; kernel-based virtual machine.

| | |
|---|---|
| **Image** | `qemux/qemu:latest` |
| **Host port** | `20136` |
| **Container port** | `20136` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Virtualization |
| **GPU** | hardware-acceleration block included (commented) |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20136>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml kvm
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
