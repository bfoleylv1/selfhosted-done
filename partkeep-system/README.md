# Partkeep System

PHP/MySQL web application; organize and manage parts inventory

| | |
|---|---|
| **Image** | `php:8.2-apache` |
| **Host port** | `20191` |
| **Container port** | `20191` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Crm |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20191>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml partkeep-system
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
