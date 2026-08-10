# Splunk (Self-Hosted)

Enterprise SIEM platform; log analysis and monitoring.

| | |
|---|---|
| **Image** | `splunk/splunk:latest` |
| **Host port** | `20292` |
| **Container port** | `8000` |
| **Category** | Security |
| **Healthcheck** | HTTP `/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20292>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml splunk
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
docker inspect --format '{{.State.Health.Status}}' splunk
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
