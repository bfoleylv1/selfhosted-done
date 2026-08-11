# Qemu

Open source emulator and virtualization; hardware emulation.

| | |
|---|---|
| **Image** | `qemux/qemu:latest` |
| **Host port** | `20228` |
| **Container port** | `20228` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Virtualization |
| **GPU** | hardware-acceleration block included (commented) |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20228>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml qemu
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
