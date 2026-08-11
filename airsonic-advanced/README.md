# Airsonic Advanced

Music server with multi-user support; stream your music anywhere

| | |
|---|---|
| **Image** | `lscr.io/linuxserver/airsonic-advanced:latest` |
| **Host port** | `20399` |
| **Container port** | `20399` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Music |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20399>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml airsonic-advanced
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
