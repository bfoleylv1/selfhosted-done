# Typesense

Typo-tolerant search engine with fast, relevant results; developer-friendly API.

| | |
|---|---|
| **Image** | `typesense/typesense:27.1` |
| **Host port** | `8108` |
| **Container port** | `8108` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:8108/health` |
| **Category** | Search Engines |
| **GPU** | hardware-acceleration block included (commented) |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:8108>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml typesense
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
