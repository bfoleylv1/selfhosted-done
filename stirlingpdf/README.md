# Stirling PDF

Stirling-PDF is a versatile, open-source toolkit that allows you to perform various PDF manipulations, such as merging, splitting, compressing, and converting PDF files.

| | |
|---|---|
| **Image** | `frooodle/s-pdf:latest` |
| **Host port** | `20609` |
| **Container port** | `8080` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Productivity |
| **Upstream** | https://github.com/Stirling-Tools/Stirling-PDF |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20609>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml stirlingpdf
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
