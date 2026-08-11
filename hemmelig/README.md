# Hemmelig

Hemmelig.app is an open-source encrypted sharing platform designed for securely transmitting sensitive information such as passwords, confidential messages, API keys, or other private data.

| | |
|---|---|
| **Image** | `hemmeligapp/hemmelig:v7` |
| **Host port** | `20580` |
| **Container port** | `3000` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://localhost:3000/api/healthz` |
| **Category** | Security |
| **Upstream** | https://github.com/HemmeligOrg/Hemmelig.app |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20580>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml hemmelig
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
