# FreshRSS

Free and open-source web RSS reader; multi-user self-hosted feed reader.

| | |
|---|---|
| **Image** | `freshrss/freshrss:latest` |
| **Host port** | `20079` |
| **Container port** | `80` |
| **Category** | Rss |
| **Healthcheck** | HTTP `/api/greader.php` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20079>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml freshrss
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
docker inspect --format '{{.State.Health.Status}}' freshrss
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
