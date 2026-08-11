# Sftp Server

SSH File Transfer Protocol; secure file transfer

| | |
|---|---|
| **Image** | `atmoz/sftp:latest` |
| **Host port** | `20275` |
| **Container port** | `20275` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | File Sharing |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20275>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml sftp-server
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
