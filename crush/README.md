# Crush

Crush is a command-line AI coding agent with shell and editor integration.

| | |
|---|---|
| **Image** | `crush/gitlab-pipeline-base:latest` |
| **Host port** | `20433` |
| **Container port** | `20433` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20433>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml crush
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
