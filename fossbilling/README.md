# FOSSBilling

Open source billing and invoicing; replacement for WHMCS.

| | |
|---|---|
| **Image** | `fossbilling/fossbilling:latest` |
| **Host port** | `20075` |
| **Container port** | `80` |
| **Category** | Crm |
| **Healthcheck** | HTTP `/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20075>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml fossbilling
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
docker inspect --format '{{.State.Health.Status}}' fossbilling
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
