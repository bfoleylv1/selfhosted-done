# Homebox

Homebox is an open-source, self-hosted home inventory and asset management application developed by SysAdmins Media.

| | |
|---|---|
| **Image** | `ghcr.io/sysadminsmedia/homebox:latest` |
| **Host port** | `7745` |
| **Container port** | `7745` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Additional Services |
| **Upstream** | https://github.com/sysadminsmedia/homebox |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:7745>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml homebox
```

## Configuration

Settings live in `.env` next to the compose file. Generated secrets are already filled in and are stable across regeneration.

## Layout

```
docker-compose.yml        # single-host deployment
swarm/docker-stack.yml    # swarm stack (named volumes, replicas, placement)
.env                      # configuration and generated secrets
```

## Check it is healthy

```bash
docker compose ps
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
