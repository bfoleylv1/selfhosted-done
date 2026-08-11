# Snort

Network intrusion detection and prevention system.

| | |
|---|---|
| **Image** | `ciscotalos/snort3:latest` |
| **Host port** | `20287` |
| **Container port** | `20287` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Security |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20287>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml snort
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
