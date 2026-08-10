# Transfer-Sh

Self-hosted service: transfer-sh

| | |
|---|---|
| **Image** | `dutchcoders/transfer.sh:latest` |
| **Host port** | `20516` |
| **Container port** | `20516` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | TCP/HTTP probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20516>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml transfer-sh
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
docker inspect --format '{{.State.Health.Status}}' transfer-sh
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
