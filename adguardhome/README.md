# AdGuard Home

AdGuard Home is a network-wide software that blocks ads and trackers.

| | |
|---|---|
| **Image** | `adguard/adguardhome:latest` |
| **Host port** | `20557` |
| **Container port** | `53` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Network |
| **Upstream** | https://github.com/AdguardTeam/AdGuardHome |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20557>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml adguardhome
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
