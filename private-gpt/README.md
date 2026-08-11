# Private Gpt

Open-source API layer turning local models into production AI apps

| | |
|---|---|
| **Image** | `3x3cut0r/privategpt:latest` |
| **Host port** | `20220` |
| **Container port** | `20220` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Ai |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20220>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml private-gpt
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
