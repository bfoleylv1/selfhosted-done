# Puppet

Configuration management tool; declarative infrastructure automation

| | |
|---|---|
| **Image** | `puppet/puppetserver:latest` |
| **Host port** | `20224` |
| **Container port** | `8080` |
| **Category** | Automation |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20224>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml puppet
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
docker inspect --format '{{.State.Health.Status}}' puppet
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
