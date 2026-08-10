# Cloud Foundry

Cloud-native platform; PaaS for app deployment

| | |
|---|---|
| **Image** | `alpine:3.20` |
| **Host port** | `20031` |
| **Container port** | `8080` |
| **Category** | Monitoring |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20031>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml cloud-foundry
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
docker inspect --format '{{.State.Health.Status}}' cloud-foundry
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
