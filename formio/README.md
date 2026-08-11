# Formio

Form and API platform for building data-driven forms and apps

| | |
|---|---|
| **Image** | `formio/formio:latest` |
| **Host port** | `3001` |
| **Container port** | `3001` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:3001>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml formio
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
