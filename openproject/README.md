# Openproject

Project management web application; issue tracking and agile tools.

| | |
|---|---|
| **Image** | `openproject/openproject:15` |
| **Host port** | `20178` |
| **Container port** | `20178` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Productivity |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20178>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml openproject
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
