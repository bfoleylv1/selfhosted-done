# Odoo

All-in-one business management suite; CRM, ERP, CMS, and more

| | |
|---|---|
| **Image** | `odoo:17` |
| **Host port** | `8069` |
| **Container port** | `8069` |
| **Category** | Crm |
| **Healthcheck** | HTTP `/web/health` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:8069>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml odoo
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
docker inspect --format '{{.State.Health.Status}}' odoo
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
