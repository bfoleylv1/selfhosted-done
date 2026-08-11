# Ackee

Lightweight anonymised web analytics; self-hosted solution.

| | |
|---|---|
| **Image** | `electerious/ackee:latest` |
| **Host port** | `20394` |
| **Container port** | `3000` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:3000/` |
| **Category** | Analytics |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20394>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml ackee
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
