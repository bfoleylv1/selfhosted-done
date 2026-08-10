# Samba

SMB/CIFS file sharing; access from Windows and Linux

| | |
|---|---|
| **Image** | `dperson/samba:latest` |
| **Host port** | `20265` |
| **Container port** | `445` |
| **Category** | File Sharing |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20265>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml samba
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
docker inspect --format '{{.State.Health.Status}}' samba
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
