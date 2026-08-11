# Opennebula

Open source cloud management platform; IaaS solution.

| | |
|---|---|
| **Image** | `opennebula/opennebula:latest` |
| **Host port** | `9869` |
| **Container port** | `9869` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Network |
| **GPU** | hardware-acceleration block included (commented) |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:9869>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml opennebula
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
