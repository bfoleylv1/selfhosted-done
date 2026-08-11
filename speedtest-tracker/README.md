# Speedtest Tracker

Speedtest Tracker is an open-source, self-hosted tool designed to regularly test and monitor your internet connection speed.

| | |
|---|---|
| **Image** | `lscr.io/linuxserver/speedtest-tracker:latest` |
| **Host port** | `20608` |
| **Container port** | `8888` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Network |
| **Upstream** | https://github.com/alexjustesen/speedtest-tracker |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20608>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml speedtest-tracker
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
