# CyberChef

CyberChef is an open-source web application designed to simplify the process of carrying out complex data analysis and encoding/decoding operations.

| | |
|---|---|
| **Image** | `ghcr.io/gchq/cyberchef:latest` |
| **Host port** | `20565` |
| **Container port** | `8080` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Security |
| **Upstream** | https://github.com/gchq/CyberChef |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20565>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml cyberchef
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
