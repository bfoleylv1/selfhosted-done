# Jan

Desktop app for running open-source models locally with GPU acceleration.

| | |
|---|---|
| **Image** | `python:3.11-slim` |
| **Host port** | `1337` |
| **Container port** | `1337` |
| **Category** | Ai |
| **Healthcheck** | TCP port probe |
| **Hardware acceleration** | GPU compute |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:1337>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml jan
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
docker inspect --format '{{.State.Health.Status}}' jan
```

## Hardware acceleration

This service can use a GPU for GPU compute. `docker-compose.yml` contains
ready-made blocks for:

- NVIDIA CUDA
- Intel oneAPI / OpenVINO
- AMD ROCm

They ship disabled. The comment convention is:

- `#` single hash = real config → **delete the hash to enable**
- `##` double hash = human comment → leave it alone

Uncomment only the block matching your hardware, then recreate:

```bash
docker compose up -d --force-recreate
```

NVIDIA needs the
[nvidia-container-toolkit](https://github.com/NVIDIA/nvidia-container-toolkit).
Intel/AMD VAAPI needs `/dev/dri` on the host and your user in the
`video`/`render` groups.

Under Swarm, `devices:` and `runtime:` are ignored — see the commented
`generic_resources` block in `swarm/docker-stack.yml`.

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
