# Salut A Toi

Multipurpose XMPP/Jabber client and ecosystem

| | |
|---|---|
| **Image** | `alpine:3.20` |
| **Host port** | `20263` |
| **Container port** | `20263` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20263>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml salut-a-toi
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
