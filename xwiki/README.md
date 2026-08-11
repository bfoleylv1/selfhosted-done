# XWiki

XWiki is a powerful open-source wiki platform designed for collaboration, knowledge management, and building custom web applications.

| | |
|---|---|
| **Image** | `xwiki:stable-mariadb-tomcat` |
| **Host port** | `20616` |
| **Container port** | `80` |
| **Containers** | 2 (app + db) |
| **Healthcheck** | HTTP `http://127.0.0.1:80/` |
| **Category** | Content Management Systems |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20616>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml xwiki
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
