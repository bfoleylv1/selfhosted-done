# Keycloak

Open-source Identity and Access Management; OAuth2, OIDC, SAML provider.

| | |
|---|---|
| **Image** | `quay.io/keycloak/keycloak:latest` |
| **Host port** | `20125` |
| **Container port** | `8080` |
| **Containers** | 1 |
| **Healthcheck** | HTTP `http://127.0.0.1:8080/realms/master` |
| **Category** | Authentication |

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
```

## Check it is healthy

```bash
docker compose ps
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.
