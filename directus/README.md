# Directus

Open-source Data Platform; turn any SQL database into a CMS.

| | |
|---|---|
| **Image** | `directus/directus:latest` |
| **Host port** | `8055` |
| **Container port** | `8055` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:8055/server/health` |
| **Category** | Content Management Systems |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:8055>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml directus
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
