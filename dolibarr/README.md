# Dolibarr

Web app to manage business activities; ERP/CRM for small companies.

| | |
|---|---|
| **Image** | `dolibarr/dolibarr:latest` |
| **Host port** | `20048` |
| **Container port** | `80` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:80/` |
| **Category** | Crm |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20048>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml dolibarr
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
