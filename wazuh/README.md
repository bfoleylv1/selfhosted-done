# Wazuh

Open source security platform; XDR and SIEM capabilities.

| | |
|---|---|
| **Image** | `wazuh/wazuh-manager:4.9.2` |
| **Host port** | `55000` |
| **Container port** | `55000` |
| **Containers** | 1 |
| **Healthcheck** | command probe |
| **Category** | Security |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:55000>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml wazuh
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
