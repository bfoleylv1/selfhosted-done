# Readarr

Book/PDF/EPUB/MOBI/AZW3 article librarian; manages book torrents and Usenet.

| | |
|---|---|
| **Image** | `lscr.io/linuxserver/readarr:develop` |
| **Host port** | `20235` |
| **Container port** | `8787` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:8787/` |
| **Category** | Audio |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20235>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml readarr
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
