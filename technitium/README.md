# Technitium

Technitium DNS Server information about Technitium...

| | |
|---|---|
| **Image** | `technitium/dns-server:latest` |
| **Host port** | `5380` |
| **Container port** | `5380` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Network |
| **Upstream** | https://github.com/TechnitiumSoftware/DnsServer |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:5380>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml technitium
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
