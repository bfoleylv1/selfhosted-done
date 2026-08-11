# Prowlarr

Indexing manager for Sonarr, Radarr, Lidarr, and Readarr; manages indexers.

| | |
|---|---|
| **Image** | `lscr.io/linuxserver/prowlarr:latest` |
| **Host port** | `9696` |
| **Container port** | `9696` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:9696/` |
| **Category** | Audio |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:9696>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml prowlarr
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
