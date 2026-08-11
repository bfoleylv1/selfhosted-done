# Lesspass

Generate passwords from master password; deterministic password generator.

| | |
|---|---|
| **Image** | `node:20-alpine` |
| **Host port** | `20138` |
| **Container port** | `20138` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Password Management |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20138>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml lesspass
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
