# WriteFreely

Federated publishing platform; write and share articles.

| | |
|---|---|
| **Image** | `writeas/writefreely:latest` |
| **Host port** | `20371` |
| **Container port** | `8080` |
| **Category** | Social |
| **Healthcheck** | HTTP `/` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20371>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml writefreely
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
docker inspect --format '{{.State.Health.Status}}' writefreely
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
