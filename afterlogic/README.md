# Afterlogic

Webmail program; modern webmail with calendar.

| | |
|---|---|
| **Image** | `php:8.2-apache` |
| **Host port** | `20397` |
| **Container port** | `20397` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Email |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20397>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml afterlogic
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
