# Apache Apisix

Real-time API gateway; built on etcd and Lua

| | |
|---|---|
| **Image** | `apache/apisix:latest` |
| **Host port** | `9080` |
| **Container port** | `9080` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Api Management |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:9080>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml apache-apisix
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
