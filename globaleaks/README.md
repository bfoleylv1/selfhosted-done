# Globaleaks

Open-source whistleblowing / secure submission platform

| | |
|---|---|
| **Image** | `globaleaks/globaleaks:latest` |
| **Host port** | `20096` |
| **Container port** | `8080` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | HTTP `/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20096>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml globaleaks
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
docker inspect --format '{{.State.Health.Status}}' globaleaks
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
