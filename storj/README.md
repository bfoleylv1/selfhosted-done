# Storj

Decentralized cloud storage; peer-to-peer storage network.

| | |
|---|---|
| **Image** | `storjlabs/storagenode:latest` |
| **Host port** | `14002` |
| **Container port** | `14002` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Backup |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:14002>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml storj
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
