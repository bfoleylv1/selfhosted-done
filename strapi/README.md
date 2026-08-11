# Strapi

Headless CMS; customizable and API-first.

| | |
|---|---|
| **Image** | `naskio/strapi:latest` |
| **Host port** | `20303` |
| **Container port** | `1337` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:1337/` |
| **Category** | Content Management Systems |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20303>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml strapi
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
