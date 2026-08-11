# Fossbilling

Open source billing and invoicing; replacement for WHMCS.

| | |
|---|---|
| **Image** | `fossbilling/fossbilling:latest` |
| **Host port** | `20075` |
| **Container port** | `20075` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Crm |

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
```

## Check it is healthy

```bash
docker compose ps
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
