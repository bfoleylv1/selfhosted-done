# Open WebUI

Open WebUI is a feature-rich, self-hosted AI platform that provides a ChatGPT-style interface for local and cloud-based AI models.

| | |
|---|---|
| **Image** | `ghcr.io/open-webui/open-webui:main` |
| **Host port** | `20597` |
| **Container port** | `8080` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Ai |
| **Upstream** | https://github.com/open-webui/open-webui |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20597>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml open-webui
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
