# Bazarr

Subtitle manager for Sonarr and Radarr; automatic download and management.

| | |
|---|---|
| **Image** | `lscr.io/linuxserver/bazarr:latest` |
| **Host port** | `6767` |
| **Container port** | `6767` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:6767/` |
| **Category** | Audio |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:6767>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml bazarr
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
