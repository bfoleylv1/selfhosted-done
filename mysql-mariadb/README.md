# MySQL / MariaDB

Popular relational database; MariaDB is a drop-in MySQL compatible alternative.

| | |
|---|---|
| **Image** | `mariadb:11` |
| **Host port** | `20161` |
| **Container port** | `3306` |
| **Category** | Database Management |
| **Healthcheck** | TCP port probe |

## Run it

Single host:

```bash
docker compose up -d
```

Then open <http://localhost:20161>.

Swarm:

```bash
docker stack deploy -c swarm/docker-stack.yml mysql-mariadb
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
docker inspect --format '{{.State.Health.Status}}' mysql-mariadb
```

## Homepage

[gethomepage](https://github.com/gethomepage/homepage) labels are included but
commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable
autodiscovery.
