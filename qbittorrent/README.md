# qBittorrent

qBittorrent is an open-source, cross-platform torrent client that offers a clean interface, powerful search capabilities, and support for most features found in modern BitTorrent clients.

| | |
|---|---|
| **Image** | `lscr.io/linuxserver/qbittorrent:latest` |
| **Host port** | `20603` |
| **Container port** | `8080` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | File Sharing |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20603>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml qbittorrent
```

## Configuration

Settings live in `.env` next to the compose file. Generated secrets are already filled in and are stable across regeneration.

## Layout

```
docker-compose.yml        # single-host deployment
swarm/docker-stack.yml    # swarm stack (named volumes, replicas, placement)
.env                      # configuration and generated secrets
```

## Check it is healthy

```bash
docker compose ps
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
