# Umbraco

Open-source CMS; built on .NET and ASP.NET.

| | |
|---|---|
| **Image** | `mcr.microsoft.com/dotnet/aspnet:8.0` |
| **Host port** | `20343` |
| **Container port** | `20343` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Content Management Systems |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20343>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml umbraco
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
