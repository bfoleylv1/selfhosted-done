# Agent Vault

agent-vault self-hosted service.

| | |
|---|---|
| **Image** | `hashicorp/vault:latest` |
| **Host port** | `20398` |
| **Container port** | `8200` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | HTTP `/v1/sys/health` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20398>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml agent-vault
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
docker inspect --format '{{.State.Health.Status}}' agent-vault
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
