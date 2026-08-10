# Dovecot

IMAP and POP3 server; mail delivery and retrieval.

| | |
|---|---|
| **Image** | `dovecot/dovecot:latest` |
| **Host port** | `20049` |
| **Container port** | `143` |
| **Category** | Email |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20049>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml dovecot
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
docker inspect --format '{{.State.Health.Status}}' dovecot
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
