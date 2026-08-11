# Keystone

Node.js GraphQL CMS; flexible and extensible.

| | |
|---|---|
| **Image** | `node:20-alpine` |
| **Host port** | `20127` |
| **Container port** | `20127` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Content Management Systems |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20127>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml keystone
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
