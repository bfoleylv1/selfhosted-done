# Github Ntfy

ntfy push notifications for GitHub events

| | |
|---|---|
| **Image** | `binwiederhier/ntfy:latest` |
| **Host port** | `20091` |
| **Container port** | `80` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | HTTP `/v1/health` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20091>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml github-ntfy
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
docker inspect --format '{{.State.Health.Status}}' github-ntfy
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
