# Bichon

Bichon is a self-hosted RSS feed reader with a focus on privacy and simplicity.

| | |
|---|---|
| **Image** | `rustmailer/bichon:latest` |
| **Host port** | `20527` |
| **Container port** | `20527` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20527>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml bichon
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
