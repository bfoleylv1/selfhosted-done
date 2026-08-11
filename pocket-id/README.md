# Pocket Id

Simple SSO identity provider with passkey support

| | |
|---|---|
| **Image** | `ghcr.io/pocket-id/pocket-id:latest` |
| **Host port** | `1411` |
| **Container port** | `1411` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:1411>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml pocket-id
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
