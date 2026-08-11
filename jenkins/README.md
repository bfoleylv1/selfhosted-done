# Jenkins

Open source automation server; CI/CD for builds and tests.

| | |
|---|---|
| **Image** | `jenkins/jenkins:lts` |
| **Host port** | `20119` |
| **Container port** | `8080` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:8080/` |
| **Category** | Development |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20119>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml jenkins
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
