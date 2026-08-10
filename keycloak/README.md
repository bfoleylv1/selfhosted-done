# Keycloak

Open-source Identity and Access Management; OAuth2, OIDC, SAML provider.

| | |
|---|---|
| **Image** | `quay.io/keycloak/keycloak:latest` |
| **Host port** | `20125` |
| **Container port** | `8080` |
| **Category** | Authentication |
| **Healthcheck** | HTTP `/health/ready` |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20125>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml keycloak
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
docker inspect --format '{{.State.Health.Status}}' keycloak
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
