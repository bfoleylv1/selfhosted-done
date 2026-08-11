# Metager

German metasearch engine; privacy-focused search results.

| | |
|---|---|
| **Image** | `php:8.2-fpm` |
| **Host port** | `20153` |
| **Container port** | `20153` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Search Engines |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20153>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml metager
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
