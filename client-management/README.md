# Client Management

Invoice, quotes, and client management for freelancers and agencies

| | |
|---|---|
| **Image** | `php:8.2-apache` |
| **Host port** | `20030` |
| **Container port** | `8080` |
| **Category** | Crm |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20030>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml client-management
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
docker inspect --format '{{.State.Health.Status}}' client-management
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
