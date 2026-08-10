# selfhosted-done

Docker Compose and Docker Swarm files for self-hosted services that have been
**started and verified working**. Each service moves into this repo only after it
actually comes up.

Every service folder is self-contained and has the same shape:

```
<service>/
├── docker-compose.yml        # single-host deployment
├── swarm/docker-stack.yml    # docker stack deploy
├── config/                   # mounted to /config
└── data/                     # mounted to /data
```

## Services

| Service | Image | Port | Description |
|---|---|---|---|
| [92five](./92five) | `php:8.2-apache` | `20401` → `80` | Self-hosted project management application. |
| [Ackee](./ackee) | `electerious/ackee:latest` | `20402` → `3000` | Lightweight anonymised web analytics; self-hosted solution. |
| [Adminer](./adminer) | `adminer:latest` | `20403` → `8080` | Tool for managing MySQL, PostgreSQL, SQLite, and other databases. |
| [Agent Vault](./agent-vault) | `hashicorp/vault:latest` | `20404` → `8200` | HashiCorp Vault - secrets management and encryption as a service. |
| [Bamboo](./bamboo) | `atlassian/bamboo:latest` | `8085` → `8085` | Atlassian Bamboo - CI/CD build and deployment server. |
| [Chef](./chef) | `chef/chef:latest` | `20405` → `443` | Automation platform for the most demanding environments. |

## Usage

Single host:

```bash
cd <service>
docker compose up -d
```

Swarm cluster:

```bash
cd <service>/swarm
docker stack deploy -c docker-stack.yml <service>
```

## Conventions

**Images** — every image reference is verified to exist and be anonymously
pullable from its registry. No invented `name/name:latest` placeholders.

**Ports** — each service publishes a unique host port so the whole library can
run side by side without collisions. The container port is the real upstream
default.

**Healthchecks** — every service has one. HTTP services probe a real endpoint
that the image actually serves; services without an HTTP surface use a TCP
port probe.

**Homepage labels** — included on every service but commented out, ready for
[gethomepage](https://github.com/gethomepage/homepage) autodiscovery. Uncomment
the `labels:` block to enable.

**Hardware acceleration** — services that can use a GPU ship commented-out
blocks for Intel QSV/VAAPI, AMD VAAPI/ROCm, and NVIDIA. The convention is:

- `#` single hash = real config — delete the hash to enable it
- `##` double hash = a human comment — leave it alone

Uncomment only the block matching your hardware. Example for Intel Quick Sync:

```yaml
    devices:
      - /dev/dri:/dev/dri
    group_add:
      - "video"
      - "render"
    environment:
      - LIBVA_DRIVER_NAME=iHD
```

NVIDIA additionally needs the
[nvidia-container-toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)
on the host.

Under Swarm, `devices:` and `runtime:` are ignored — GPUs are requested through
`generic_resources`, and the node must advertise the GPU in
`/etc/docker/daemon.json`. Each swarm file documents this inline.

## Notes

Services that need a companion database (PostgreSQL, MySQL, Redis) ship as a
single container here. Add the database service to the compose file, or point
the service at an existing one, before expecting it to report healthy.
