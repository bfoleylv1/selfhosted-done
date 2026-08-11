# IT-Tools

IT-Tools is an open-source collection of online utilities designed for developers and IT professionals.

| | |
|---|---|
| **Image** | `corentinth/it-tools:latest` |
| **Host port** | `20584` |
| **Container port** | `80` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Development |
| **Upstream** | https://github.com/CorentinTh/it-tools |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20584>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml it-tools
```

## Configuration

Settings live in `.env` next to the compose file. Generated secrets are already filled in and are stable across regeneration.

## Layout

```
docker-compose.yml        # single-host deployment
swarm/docker-stack.yml    # swarm stack (named volumes, replicas, placement)
.env                      # configuration and generated secrets
```

## Check it is healthy

```bash
docker compose ps
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
