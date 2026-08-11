# Sogo

Web access to IMAP and CalDAV; groupware solution.

| | |
|---|---|
| **Image** | `debian:12-slim` |
| **Host port** | `20000` |
| **Container port** | `20000` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Email |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20000>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml sogo
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
