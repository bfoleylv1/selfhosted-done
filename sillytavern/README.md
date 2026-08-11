# Sillytavern

SillyTavern is a self-hosted, feature-rich UI for chatting with LLMs and character cards.

| | |
|---|---|
| **Image** | `ghcr.io/sillytavern/sillytavern:latest` |
| **Host port** | `20555` |
| **Container port** | `20555` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20555>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml sillytavern
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
