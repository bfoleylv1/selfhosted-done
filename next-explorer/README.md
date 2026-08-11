# Next Explorer

NextExplorer is a modern, self-hosted file explorer designed for teams, creative agencies, and homelabs that need both a polished user interface and fine-grained access control.

| | |
|---|---|
| **Image** | `nxzai/explorer:latest` |
| **Host port** | `20595` |
| **Container port** | `3000` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:3000/` |
| **Category** | File |
| **Upstream** | https://github.com/nxzai/NextExplorer |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20595>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml next-explorer
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
