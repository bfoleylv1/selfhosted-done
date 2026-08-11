# rmux

Migrated from `self-hosted-2` but **no valid container image could be confirmed** this session — image discovery (web search, GitHub raw, Docker Hub search) was unavailable or returned only guessed names that failed registry verification.

The auto-derived `image:` has been commented out so it cannot be pulled by accident. Before deploying, confirm the real image from the project's upstream docs, set it in `docker-compose.yml` and `swarm/docker-stack.yml`, then run `.tools/sync.py`.
