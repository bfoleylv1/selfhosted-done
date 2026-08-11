# Instapaper

Web article saver; read later and save content

| | |
|---|---|
| **Image** | `alpine:3.20` |
| **Host port** | `20116` |
| **Container port** | `20116` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | News |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20116>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml instapaper
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
