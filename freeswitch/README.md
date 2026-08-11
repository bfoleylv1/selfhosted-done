# Freeswitch

Open-source telephony platform / softswitch (VoIP)

| | |
|---|---|
| **Image** | `safarov/freeswitch:latest` |
| **Host port** | `20078` |
| **Container port** | `20078` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20078>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml freeswitch
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
