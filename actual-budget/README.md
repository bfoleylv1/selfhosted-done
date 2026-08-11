# Actual Budget

Actual Budget is an open-source, self-hosted personal finance and budgeting app focused on privacy and control.

| | |
|---|---|
| **Image** | `docker.io/actualbudget/actual-server:latest` |
| **Host port** | `5006` |
| **Container port** | `5006` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Additional Services |
| **Upstream** | https://github.com/actualbudget/actual |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:5006>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml actual-budget
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
