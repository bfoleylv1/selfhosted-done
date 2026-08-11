# Logstash

Data processing pipeline; collect, transform, and forward data.

| | |
|---|---|
| **Image** | `docker.elastic.co/logstash/logstash:8.15.0` |
| **Host port** | `9600` |
| **Container port** | `9600` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:9600/` |
| **Category** | Analytics |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:9600>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml logstash
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
