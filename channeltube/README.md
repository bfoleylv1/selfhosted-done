# Channeltube

Channel Tube (Conductor) aggregates and serves YouTube channel content as a self-hosted library.

| | |
|---|---|
| **Image** | `thewicklowwolf/channeltube:latest` |
| **Host port** | `20423` |
| **Container port** | `20423` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20423>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml channeltube
```

## Layout

```
docker-compose.yml        # single-host deployment
swarm/docker-stack.yml    # swarm stack (named volumes, replicas, placement)
```

## Check it is healthy

```bash
docker compose ps
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
