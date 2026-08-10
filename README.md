# selfhosted-done

Docker Compose and Docker Swarm files for self-hosted services that have been
**started and verified working**. A service lands here only after it actually
comes up.

Currently **10 services**.

Every service folder has the same shape:

```
<service>/
├── docker-compose.yml        # single-host deployment
├── swarm/docker-stack.yml    # docker stack deploy
├── config/                   # mounted to /config
└── data/                     # mounted to /data
```

## Services

| Service | Image | Port | GPU | Description |
|---|---|---|:--:|---|
| [92five](./92five) | `php:8.2-apache` | `20400` → `80` | — | Self-hosted project management application. |
| [Ackee](./ackee) | `electerious/ackee:latest` | `20401` → `3000` | — | Lightweight anonymised web analytics; self-hosted solution. |
| [Adminer](./adminer) | `adminer:latest` | `20402` → `8080` | — | Tool for managing MySQL, PostgreSQL, SQLite, and other databases. |
| [Adyen Proxy](./adyen-proxy) | `node:20-alpine` | `20403` → `3000` | — | Proxy service for the Adyen payments API. |
| [OpenAFS](./afs) | `alpine:3.20` | `7000` → `7000` | — | OpenAFS distributed network filesystem. |
| [Afterlogic](./afterlogic) | `php:8.2-apache` | `20001` → `80` | — | Webmail program; modern webmail with calendar. |
| [Agent Vault](./agent-vault) | `hashicorp/vault:latest` | `20404` → `8200` | — | HashiCorp Vault - secrets management and encryption as a service. |
| [Airsonic Advanced](./airsonic-advanced) | `airsonicadvanced/airsonic-advanced:latest` | `4040` → `4040` | ✅ | Music server with multi-user support; stream your music anywhere. |
| [Bamboo](./bamboo) | `atlassian/bamboo:latest` | `8085` → `8085` | — | Atlassian Bamboo - CI/CD build and deployment server. |
| [Chef](./chef) | `chef/chef:latest` | `20405` → `443` | — | Automation platform for the most demanding environments. |

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

**Images** — every image reference was checked against its registry and is
anonymously pullable. No invented `name/name:latest` placeholders.

**Ports** — each service gets a unique host port so the whole library can run
side by side without collisions. The container port is the real upstream default.

**Healthchecks** — every service has one. HTTP services probe an endpoint the
image actually serves; services with no HTTP surface use a TCP port probe.

**Homepage labels** — present on every service, commented out, ready for
[gethomepage](https://github.com/gethomepage/homepage). Uncomment the `labels:`
block to enable autodiscovery.

## Hardware acceleration

Services that can use a GPU ship commented-out blocks for Intel QSV/VAAPI,
AMD VAAPI/ROCm, and NVIDIA. The comment convention is:

- `#` single hash = real config → delete the hash to enable
- `##` double hash = human comment → leave it alone

Uncomment only the block matching your hardware. Intel Quick Sync example:

```yaml
    devices:
      - /dev/dri:/dev/dri
    group_add:
      - "video"
      - "render"
    environment:
      - LIBVA_DRIVER_NAME=iHD
```

NVIDIA also needs the
[nvidia-container-toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)
on the host.

Under Swarm, `devices:` and `runtime:` are ignored — GPUs are requested via
`generic_resources` and the node must advertise the GPU in
`/etc/docker/daemon.json`. Each swarm file documents this inline.

## Notes

Services that need a companion database (PostgreSQL, MySQL, Redis) ship as a
single container. Add the database to the compose file, or point the service at
an existing one, before expecting a healthy status.
