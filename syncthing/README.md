# Syncthing

Continuous file synchronization; peer-to-peer sync without central server.

| | |
|---|---|
| **Image** | `lscr.io/linuxserver/syncthing:latest` |
| **Host port** | `8384` |
| **Container port** | `8384` |
| **Category** | File |
| **Healthcheck** | HTTP `/rest/noauth/health` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:8384>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml syncthing
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
docker inspect --format '{{.State.Health.Status}}' syncthing
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
