# Iredmail

Complete mail server solution; quick and easy setup

| | |
|---|---|
| **Image** | `ubuntu:24.04` |
| **Host port** | `20114` |
| **Container port** | `20114` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Email |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20114>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml iRedMail
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
