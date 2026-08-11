# Vikunja

Vikunja is an open-source, self-hosted task management and to-do list application designed as a privacy-focused alternative to tools like Todoist, Trello, and Asana.

| | |
|---|---|
| **Image** | `vikunja/vikunja:latest` |
| **Host port** | `20614` |
| **Container port** | `3456` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:3456/` |
| **Category** | Productivity |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20614>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml vikunja
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
