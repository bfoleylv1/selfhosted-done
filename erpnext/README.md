# ERPNext

Open source ERP; built on Frappe framework for business management

| | |
|---|---|
| **Image** | `frappe/erpnext:latest` |
| **Host port** | `20063` |
| **Container port** | `8000` |
| **Category** | Crm |
| **Healthcheck** | HTTP `/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20063>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml erpnext
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
docker inspect --format '{{.State.Health.Status}}' erpnext
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
