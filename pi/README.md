# Pi

Pi is an OpenAI-hosted experimental personal AI (no self-hosted image).

| | |
|---|---|
| **Image** | `(unset)` |
| **Host port** | `20493` |
| **Container port** | `20493` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Self Hosting Solutions |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20493>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml pi
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
