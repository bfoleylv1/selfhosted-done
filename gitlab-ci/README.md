# Gitlab Ci

Built-in CI/CD for GitLab; automated testing and deployment

| | |
|---|---|
| **Image** | `gitlab/gitlab-runner:latest` |
| **Host port** | `8093` |
| **Container port** | `8093` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Development |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:8093>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml gitlab-ci
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
