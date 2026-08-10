# Suricata

Network threat detection engine; IDS/IPS/NSM.

| | |
|---|---|
| **Image** | `jasonish/suricata:latest` |
| **Host port** | `20315` |
| **Container port** | `8080` |
| **Category** | Security |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20315>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml suricata
```

## Layout

```
docker-compose.yml        # single-host deployment
swarm/docker-stack.yml    # swarm stack (named volumes, replicas, placement)
config/                   # mounted to /config
data/                     # mounted to /data
```

## Check it is healthy

```bash
docker inspect --format '{{.State.Health.Status}}' suricata
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
