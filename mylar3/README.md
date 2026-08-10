# Mylar3

Mylar3: automated Comic Book (CBZ/CBR) downloader and manager

| | |
|---|---|
| **Image** | `linuxserver/mylar3:latest` |
| **Host port** | `20539` |
| **Container port** | `20539` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20539>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml mylar3
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
docker inspect --format '{.State.Health.Status}' mylar3
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
