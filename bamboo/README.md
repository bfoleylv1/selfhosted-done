# Bamboo

Atlassian continuous integration and deployment server (commercial)

| | |
|---|---|
| **Image** | `atlassian/bamboo:latest` |
| **Host port** | `8085` |
| **Container port** | `8085` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:8085>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml bamboo
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
