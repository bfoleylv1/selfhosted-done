# Beszel Agent

The Beszel Agent is the client-side component that connects to the Hub to send and receive messages.

| | |
|---|---|
| **Image** | `henrygd/beszel-agent:latest` |
| **Host port** | `45876` |
| **Container port** | `45876` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Monitoring |
| **Upstream** | https://github.com/henrygd/beszel |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:45876>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml beszel-agent
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
