# OIDC Proxy

Single sign-on solution for legacy applications using OAuth2/OIDC

| | |
|---|---|
| **Image** | `quay.io/oauth2-proxy/oauth2-proxy:latest` |
| **Host port** | `4180` |
| **Container port** | `4180` |
| **Category** | Authentication |
| **Healthcheck** | HTTP `/ping` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:4180>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml oidc-proxy
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
docker inspect --format '{{.State.Health.Status}}' oidc-proxy
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
