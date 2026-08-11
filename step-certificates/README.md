# Step Certificates

Private CA; X.509 PKI and ACME server

| | |
|---|---|
| **Image** | `smallstep/step-ca:latest` |
| **Host port** | `20301` |
| **Container port** | `20301` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Security |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20301>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml step-certificates
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
