# Workadventure

Collaborative virtual office / worlds (MMORPG-style)

| | |
|---|---|
| **Image** | `thecodingmachine/workadventure-play:master` |
| **Host port** | `20370` |
| **Container port** | `20370` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20370>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml workadventure
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
