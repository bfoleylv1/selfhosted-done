# Nomad

Workload orchestrator; schedule and run containers and VMs.

| | |
|---|---|
| **Image** | `hashicorp/nomad:latest` |
| **Host port** | `4646` |
| **Container port** | `4646` |
| **Category** | Automation |
| **Healthcheck** | HTTP `/v1/status/leader` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:4646>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml nomad
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
docker inspect --format '{{.State.Health.Status}}' nomad
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
