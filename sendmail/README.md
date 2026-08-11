# Sendmail

Most widely used Unix mail transfer agent.

| | |
|---|---|
| **Image** | `debian:12-slim` |
| **Host port** | `20270` |
| **Container port** | `20270` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Email |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20270>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml sendmail
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
