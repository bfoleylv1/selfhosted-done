# Matchering

Matchering is a web app for automatic audio mastering using a reference track.

| | |
|---|---|
| **Image** | `sergree/matchering-web:latest` |
| **Host port** | `20472` |
| **Container port** | `20472` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20472>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml matchering
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
