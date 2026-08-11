# Pihole

Pi-hole is a network-wide ad blocker that acts as a DNS sinkhole, filtering out ads and trackers across all devices on your local network.

| | |
|---|---|
| **Image** | `pihole/pihole:latest` |
| **Host port** | `20600` |
| **Container port** | `80` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Network |
| **Upstream** | https://github.com/pi-hole/pi-hole |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20600>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml pihole
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
