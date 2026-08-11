# Chef

Automation platform for the most demanding environments.

| | |
|---|---|
| **Image** | `chef/chef:latest` |
| **Host port** | `20405` |
| **Container port** | `20405` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Automation |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20405>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml chef
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
