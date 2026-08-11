# Hashicorp Vault

Secrets management and encryption; secure key storage

| | |
|---|---|
| **Image** | `hashicorp/vault:latest` |
| **Host port** | `20109` |
| **Container port** | `20109` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Security |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20109>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml hashicorp-vault
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
