# Node-RED

Node-RED is a low-code programming tool for event-driven applications, designed to connect devices, APIs, and online services through an intuitive, browser-based flow editor.

| | |
|---|---|
| **Image** | `nodered/node-red:latest` |
| **Host port** | `20596` |
| **Container port** | `1080` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Automation |
| **Upstream** | https://github.com/node-red/node-red |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20596>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml nodered
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
