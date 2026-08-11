# Nessus

Nessus is one of the most widely used vulnerability assessment tools, designed to help identify and remediate security issues in IT environments.

| | |
|---|---|
| **Image** | `tenable/nessus:latest-ubuntu` |
| **Host port** | `8834` |
| **Container port** | `8834` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Security |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:8834>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml nessus
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
