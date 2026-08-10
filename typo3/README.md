# Typo3

Open-source CMS; enterprise-grade content management.

| | |
|---|---|
| **Image** | `ghcr.io/typo3/core-testing-php82:latest` |
| **Host port** | `20341` |
| **Container port** | `80` |
| **Category** | Content Management Systems |
| **Healthcheck** | HTTP `/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20341>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml typo3
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
docker inspect --format '{{.State.Health.Status}}' typo3
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
