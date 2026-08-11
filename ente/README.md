# Ente

Ente is an end-to-end encrypted photos and 2FA authenticator service you can self-host.

| | |
|---|---|
| **Image** | `tbindustries/ente:latest` |
| **Host port** | `20440` |
| **Container port** | `20440` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20440>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml ente
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
