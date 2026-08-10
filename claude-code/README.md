# Claude Code

Claude Code: Anthropic's agentic CLI for coding tasks (self-hosted wrapper)

| | |
|---|---|
| **Image** | `anthropics/claude-code:latest` |
| **Host port** | `20530` |
| **Container port** | `20530` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20530>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml claude-code
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
docker inspect --format '{.State.Health.Status}' claude-code
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
