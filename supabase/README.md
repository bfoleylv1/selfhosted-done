# Supabase

Firebase alternative; open-source backend for web apps.

| | |
|---|---|
| **Image** | `supabase/postgres:15.8.1.020` |
| **Host port** | `20310` |
| **Container port** | `8000` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:8000/health` |
| **Category** | Database Tools |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20310>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml supabase
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
