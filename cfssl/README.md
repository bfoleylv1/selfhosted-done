# Cfssl

CloudFlare's PKI toolkit; certificate authority and tools.

| | |
|---|---|
| **Image** | `cfssl/cfssl:latest` |
| **Host port** | `8888` |
| **Container port** | `8888` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Security |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:8888>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml cfssl
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
