# Streama

Self-hosted Netflix clone; organize and stream your media collection.

| | |
|---|---|
| **Image** | `eclipse-temurin:17-jre` |
| **Host port** | `20304` |
| **Container port** | `8080` |
| **Category** | Audio |
| **Healthcheck** | TCP port probe |
| **Hardware acceleration** | video transcoding |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20304>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml streama
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
docker inspect --format '{{.State.Health.Status}}' streama
```

## Hardware acceleration

This service can use a GPU for video transcoding. `docker-compose.yml` contains
ready-made blocks for:

- Intel Quick Sync / VAAPI
- AMD VAAPI
- NVIDIA NVENC/NVDEC

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
