# Libvirt

Open source virtualization API; manage VMs and containers.

| | |
|---|---|
| **Image** | `ubuntu:24.04` |
| **Host port** | `16509` |
| **Container port** | `16509` |
| **Category** | Virtualization |
| **Healthcheck** | TCP port probe |
| **Hardware acceleration** | device passthrough |

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
config/                   # mounted to /config
data/                     # mounted to /data
```

## Check it is healthy

```bash
docker inspect --format '{{.State.Health.Status}}' libvirt
```

## Hardware acceleration

This service can use a GPU for device passthrough. `docker-compose.yml` contains
ready-made blocks for:

- KVM / VFIO passthrough

They ship disabled. The comment convention is:

- `#` single hash = real config → **delete the hash to enable**
- `##` double hash = human comment → leave it alone

Uncomment only the block matching your hardware, then recreate:

```bash
docker compose up -d --force-recreate
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
