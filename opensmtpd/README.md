# OpenSMTPD

SMTP server; OpenBSD's mail server

| | |
|---|---|
| **Image** | `debian:12-slim` |
| **Host port** | `20182` |
| **Container port** | `25` |
| **Category** | Email |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20182>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml opensmtpd
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
docker inspect --format '{{.State.Health.Status}}' opensmtpd
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
