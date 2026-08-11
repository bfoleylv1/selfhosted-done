# Linkding

Linkding is a lightweight, self-hosted bookmark manager designed to simplify saving and organizing links.

| | |
|---|---|
| **Image** | `sissbruecker/linkding:latest` |
| **Host port** | `20588` |
| **Container port** | `9090` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:9090/login/` |
| **Category** | News |
| **Upstream** | https://github.com/sissbruecker/linkding |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20588>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml linkding
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
