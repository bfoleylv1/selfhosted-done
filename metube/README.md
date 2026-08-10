# Metube

MeTube: self-hosted YouTube-dl / yt-dlp web UI for downloading media

| | |
|---|---|
| **Image** | `alexta69/metube:latest` |
| **Host port** | `20475` |
| **Container port** | `20475` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20475>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml metube
```

## Layout

```
docker-compose.yml        # single-host deployment
swarm/docker-stack.yml    # swarm stack (named volumes, replicas, placement)
config/                   # mounted to /config
data/                     # mounted to /data
```

## Check it is healthy

```bash
docker inspect --format '{.State.Health.Status}' metube
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
