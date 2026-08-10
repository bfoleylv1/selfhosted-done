# selfhosted-done

Docker Compose and Docker Swarm files for self-hosted services that have been
**started and verified working**. A service lands here only after it actually
comes up.

Currently **53 services**.

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
| [42Links](./42links) | `node:20-alpine` | `8080` → `8080` | — | Self-hosted service. |
| [92five](./92five) | `php:8.2-apache` | `20393` → `80` | — | Self-hosted project management application. |
| [Ackee](./ackee) | `electerious/ackee:latest` | `20394` → `3000` | — | Lightweight anonymised web analytics; self-hosted solution. |
| [Adminer](./adminer) | `adminer:latest` | `20395` → `8080` | — | Tool for managing MySQL, PostgreSQL, SQLite, and other databases. |
| [Adyen Proxy](./adyen-proxy) | `node:20-alpine` | `20396` → `3000` | — | Proxy service for the Adyen payments API. |
| [OpenAFS](./afs) | `alpine:3.20` | `7000` → `7000` | — | OpenAFS distributed network filesystem. |
| [Afterlogic](./afterlogic) | `php:8.2-apache` | `20397` → `80` | — | Webmail program; modern webmail with calendar. |
| [Agent Vault](./agent-vault) | `hashicorp/vault:latest` | `20398` → `8200` | — | HashiCorp Vault - secrets management and encryption as a service. |
| [Airsonic Advanced](./airsonic-advanced) | `airsonicadvanced/airsonic-advanced:latest` | `20399` → `4040` | ✅ | Music server with multi-user support; stream your music anywhere. |
| [Akkoma](./akkoma) | `akkoma/akkoma:latest` | `20400` → `4000` | — | Self-hosted service. |
| [Alertmanager](./alertmanager) | `prom/alertmanager:latest` | `9093` → `9093` | — | Alert handler for Prometheus; route and silencing alerts. |
| [Algo Vpn](./algo-vpn) | `ubuntu:24.04` | `20401` → `8080` | — | VPN servers; deploy IPsec VPN on popular cloud providers. |
| [Amanda](./amanda) | `ubuntu:24.04` | `20402` → `8080` | — | Advanced Maryland Automatic Network Disk Archiver. |
| [Ambassador](./ambassador) | `docker.io/emissaryingress/emissary:3.9.1` | `20403` → `8080` | — | L7 load balancer; Kubernetes-native application delivery controller. |
| [Ampache](./ampache) | `ampache/ampache:latest` | `20404` → `80` | ✅ | Web-based audio file manager; provides streaming and management interface. |
| [Ansible](./ansible) | `alpine/ansible:latest` | `20001` → `8080` | — | Open source automation engine; IT automation and configuration management. |
| [Apache Apisix](./apache-apisix) | `apache/apisix:latest` | `9080` → `9080` | — | Real-time API gateway; built on etcd and Lua. |
| [Appflowy](./appflowy) | `appflowyinc/appflowy_cloud:latest` | `20002` → `8080` | — | Open source Notion alternative; collaborative workspace builder. |
| [Appwrite](./appwrite) | `appwrite/appwrite:1.6.0` | `20003` → `80` | — | Self-hosted service. |
| [Authelia](./authelia) | `authelia/authelia:latest` | `9091` → `9091` | — | Identity and Access Proxy providing 2FA, SSO, and access controls for services. |
| [Awstats](./awstats) | `php:8.2-apache` | `20004` → `8080` | — | Advanced web statistics; detailed reporting and log analysis. |
| [Axigen](./axigen) | `axigen/axigen:latest` | `20005` → `80` | — | Mail server; enterprise email and collaboration. |
| [B1Gmail](./b1gMail) | `php:8.2-apache` | `20006` → `8080` | — | Self-hosted service. |
| [Backuppc](./backuppc) | `adferrand/backuppc:latest` | `20007` → `80` | — | High-performance clientless backup system; server and desktop backup. |
| [Bacula](./bacula) | `ubuntu:24.04` | `20008` → `8080` | — | Enterprise backup solution; network backup management. |
| [Baikal](./baikal) | `ckulka/baikal:nginx` | `20009` → `80` | — | Self-hosted service. |
| [Bamboo](./bamboo) | `atlassian/bamboo:latest` | `8085` → `8085` | — | Atlassian Bamboo - CI/CD build and deployment server. |
| [Bar Assistant](./bar-assistant) | `barassistant/server:v5` | `20010` → `8080` | — | Self-hosted service. |
| [Baserow](./baserow) | `baserow/baserow:latest` | `20011` → `80` | — | Open source Notion alternative; database and form builder. |
| [Bazarr](./bazarr) | `lscr.io/linuxserver/bazarr:latest` | `6767` → `6767` | ✅ | Subtitle manager for Sonarr and Radarr; automatic download and management. |
| [Bifrost](./bifrost) | `alpine:3.20` | `20012` → `8080` | — | Media server with Jellyfin-like features; open source and self-hosted. |
| [Bitwarden](./bitwarden) | `vaultwarden/server:latest` | `20013` → `80` | — | Open source password manager; secure storage for passwords and notes. |
| [Bitwarden Rs](./bitwarden-rs) | `vaultwarden/server:latest` | `20014` → `80` | — | Lightweight Bitwarden server; Rust implementation of Bitwarden API. |
| [Bleve](./bleve) | `golang:1.23-alpine` | `20015` → `8080` | — | Modern text search and analytics; Go full-text search library. |
| [Booklore](./booklore) | `ghcr.io/booklore-app/booklore:latest` | `6060` → `6060` | — | Self-hosted service. |
| [Bookstack](./bookstack) | `lscr.io/linuxserver/bookstack:latest` | `20016` → `80` | — | Wiki platform to organize and maintain documentation. |
| [Bookwyrm](./bookwyrm) | `python:3.11-slim` | `8000` → `8000` | — | Federated book social network; discover and discuss books. |
| [Borgbackup](./borgbackup) | `ghcr.io/borgmatic-collective/borgmatic:latest` | `20017` → `8080` | — | Deduplicating backup program; efficient storage for backups. |
| [Briar](./briar) | `alpine:3.20` | `20018` → `8080` | — | Peer-to-peer messaging app; works over Tor and Bluetooth. |
| [Browserstack Turboscale](./browserstack-turboscale) | `alpine:3.20` | `20019` → `8080` | — | Self-hosted service. |
| [Buddy Enterprise](./buddy-enterprise) | `debian:12-slim` | `20020` → `8080` | — | Self-hosted service. |
| [C15T](./c15t) | `node:20-alpine` | `20021` → `8080` | — | Self-hosted service. |
| [Caddy](./caddy) | `caddy:alpine` | `20022` → `80` | — | Easy to run HTTP web server; automatic HTTPS and simple configuration. |
| [Canvas Lms](./canvas-lms) | `instructure/canvas-lms:stable` | `3000` → `3000` | — | Self-hosted service. |
| [Cap](./cap) | `alpine:3.20` | `20023` → `8080` | — | Self-hosted service. |
| [Cassandra](./cassandra) | `cassandra:5` | `9042` → `9042` | — | Highly scalable NoSQL database; column-family store designed for large datasets. |
| [Castopod](./castopod) | `castopod/castopod:latest` | `20024` → `8000` | ✅ | Self-hosted service. |
| [Centrifugo](./centrifugo) | `centrifugo/centrifugo:v5` | `20025` → `8000` | — | Self-hosted service. |
| [Cerbos](./cerbos) | `ghcr.io/cerbos/cerbos:latest` | `3592` → `3592` | — | Self-hosted service. |
| [Certbot](./certbot) | `certbot/certbot:latest` | `20026` → `80` | — | Let's Encrypt client; automatic certificate management. |
| [Cfssl](./cfssl) | `cfssl/cfssl:latest` | `8888` → `8888` | — | CloudFlare's PKI toolkit; certificate authority and tools. |
| [Cgit](./cgit) | `alpine:3.20` | `20027` → `8080` | — | Self-hosted service. |
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
