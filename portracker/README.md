# Portracker

Portracker is a simple, self-hosted port monitoring tool that helps you keep track of open ports on your servers.

| | |
|---|---|
| **Image** | `mostafawahied/portracker:latest` |
| **Host port** | `4999` |
| **Container port** | `4999` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Monitoring |
| **Upstream** | https://github.com/mostafa-wahied/portracker |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:4999>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml portracker
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
