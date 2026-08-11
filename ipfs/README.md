# Ipfs

Protocol for decentralized file sharing; distributed content addressing.

| | |
|---|---|
| **Image** | `ipfs/kubo:latest` |
| **Host port** | `5001` |
| **Container port** | `5001` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | File |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:5001>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml ipfs
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
