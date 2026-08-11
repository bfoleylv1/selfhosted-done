# Text Generation Webui

User interface for running LLMs locally; extensive model support

| | |
|---|---|
| **Image** | `atinoda/text-generation-webui:default` |
| **Host port** | `7860` |
| **Container port** | `7860` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Ai |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:7860>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml text-generation-webui
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
