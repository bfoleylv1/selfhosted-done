# Gomodel

GoModel: open-source AI gateway / control plane proxy with an OpenAI- and Anthropic-compatible API (a LiteLLM alternative)

| | |
|---|---|
| **Image** | `golang:1.23-alpine` |
| **Host port** | `20099` |
| **Container port** | `20099` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20099>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml gomodel
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
