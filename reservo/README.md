# Reservo

Self-hosted image hosting and sharing script

| | |
|---|---|
| **Image** | `reservo/reservo:latest` |
| **Host port** | `20241` |
| **Container port** | `20241` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20241>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml reservo
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
