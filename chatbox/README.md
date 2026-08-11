# Chatbox

Chatbox is a desktop and self-hosted AI chat client supporting many LLM providers.

| | |
|---|---|
| **Image** | `chatbox/docker:latest` |
| **Host port** | `20424` |
| **Container port** | `20424` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20424>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml chatbox
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
