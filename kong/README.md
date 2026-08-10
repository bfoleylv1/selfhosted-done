# Kong

Kong Gateway; cloud-native API, LLM, and MCP gateway solution

| | |
|---|---|
| **Image** | `kong:latest` |
| **Host port** | `20133` |
| **Container port** | `8000` |
| **Category** | Api Management |
| **Healthcheck** | HTTP `/status` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20133>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml kong
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
docker inspect --format '{{.State.Health.Status}}' kong
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
