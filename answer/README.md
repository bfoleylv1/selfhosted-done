# Answer

Answer: open-source knowledge management and Q&A platform (Stack Overflow alternative)

| | |
|---|---|
| **Image** | `answerdev/answer:latest` |
| **Host port** | `20411` |
| **Container port** | `20411` |
| **Category** | Self Hosting Solutions |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20411>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml answer
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
docker inspect --format '{.State.Health.Status}' answer
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
