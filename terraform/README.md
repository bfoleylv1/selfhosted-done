# Terraform

Infrastructure as code tool; provision and manage cloud resources

| | |
|---|---|
| **Image** | `hashicorp/terraform:latest` |
| **Host port** | `20322` |
| **Container port** | `8080` |
| **Category** | Automation |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20322>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml terraform
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
docker inspect --format '{{.State.Health.Status}}' terraform
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
