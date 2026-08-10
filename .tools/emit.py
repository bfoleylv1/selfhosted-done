#!/usr/bin/env python3
"""Emit a correct docker-compose.yml and swarm/docker-stack.yml for a service."""
import os, sys
TOOLS = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, TOOLS)
import facts, gpublocks


def healthcheck(port, spec, indent="    "):
    i = indent
    if spec is None:
        test = f'["CMD-SHELL", "nc -z 127.0.0.1 {port} || exit 1"]'
    elif spec.startswith("/"):
        test = (f'["CMD-SHELL", "curl -fsS http://127.0.0.1:{port}{spec} '
                f'|| wget -qO- http://127.0.0.1:{port}{spec} || exit 1"]')
    else:
        test = f'["CMD-SHELL", "{spec} || exit 1"]'
    return (f"{i}healthcheck:\n"
            f"{i}  test: {test}\n"
            f"{i}  interval: 30s\n"
            f"{i}  timeout: 10s\n"
            f"{i}  retries: 3\n"
            f"{i}  start_period: 60s")


def labels(name, desc, cats, indent="    ", href_port=None):
    i = indent
    tags = ",".join(cats) if cats else "Self Hosting Solutions"
    grp = cats[0] if cats else "Self Hosted"
    d = (desc or f"{name} self-hosted service.").replace('"', "'").strip()
    port = href_port or 8080
    return (f"{i}# labels:\n"
            f'{i}#   - "homepage.group={grp}"\n'
            f'{i}#   - "homepage.name={name}"\n'
            f'{i}#   - "homepage.description={d}"\n'
            f'{i}#   - "homepage.tags={tags}"\n'
            f'{i}#   - "homepage.icon={name}.png"\n'
            f'{i}#   - "homepage.href=http://${{HOST_IP:-localhost}}:{port}"\n'
            f'{i}#   - "homepage.server=localhost"')


def compose(name, image, port, hspec, gclass, desc, cats, host_port=None):
    hp = host_port or port or 8080
    cport = port or hp
    o = []
    o.append(f"# {name} - docker compose (single host)")
    o.append(f"# image verified to exist at generation time: {image}")
    o.append("")
    o.append("services:")
    o.append(f"  {name}:")
    o.append(f"    image: {image}")
    o.append(f"    container_name: {name}")
    o.append("    restart: unless-stopped")
    o.append("    ports:")
    o.append(f'      - "{hp}:{cport}"')
    o.append("    environment:")
    o.append("      - TZ=${TZ:-America/Los_Angeles}")
    o.append("      - PUID=${PUID:-1000}")
    o.append("      - PGID=${PGID:-1000}")
    ev = gpublocks.env_lines(gclass, "      ")
    if ev:
        o.append(ev)
    o.append("    volumes:")
    o.append("      - ./config:/config")
    o.append("      - ./data:/data")
    o.append(healthcheck(cport, hspec))
    sk = gpublocks.service_keys(gclass, "    ")
    if sk:
        o.append(sk)
    o.append(labels(name, desc, cats, href_port=hp))
    o.append("")
    o.append("networks:")
    o.append("  default:")
    o.append(f"    name: {name}_net")
    o.append("")
    return "\n".join(o)


def swarm(name, image, port, hspec, gclass, desc, cats, host_port=None):
    hp = host_port or port or 8080
    cport = port or hp
    o = []
    o.append(f"# {name} - docker swarm stack")
    o.append(f"# deploy: docker stack deploy -c docker-stack.yml {name}")
    o.append(f"# image verified to exist at generation time: {image}")
    o.append("")
    o.append("services:")
    o.append(f"  {name}:")
    o.append(f"    image: {image}")
    o.append("    ports:")
    o.append(f"      - target: {cport}")
    o.append(f"        published: {hp}")
    o.append("        protocol: tcp")
    o.append("        mode: ingress")
    o.append("    environment:")
    o.append("      - TZ=${TZ:-America/Los_Angeles}")
    o.append("      - PUID=${PUID:-1000}")
    o.append("      - PGID=${PGID:-1000}")
    ev = gpublocks.env_lines(gclass, "      ")
    if ev:
        o.append(ev)
    o.append("    volumes:")
    o.append(f"      - {name}_config:/config")
    o.append(f"      - {name}_data:/data")
    o.append(healthcheck(cport, hspec))
    o.append("    deploy:")
    o.append("      mode: replicated")
    o.append("      replicas: 1")
    o.append("      placement:")
    o.append("        constraints:")
    o.append("          - node.platform.os == linux")
    if gclass:
        o.append(gpublocks.swarm_placement_gpu("          "))
    o.append("      restart_policy:")
    o.append("        condition: on-failure")
    o.append("        delay: 5s")
    o.append("        max_attempts: 3")
    o.append("      update_config:")
    o.append("        order: start-first")
    o.append("        failure_action: rollback")
    o.append("      resources:")
    o.append("        limits:")
    o.append("          memory: 2G")
    if gclass:
        o.append(gpublocks.swarm_note("      "))
    o.append(labels(name, desc, cats, href_port=hp))
    o.append("")
    o.append("volumes:")
    o.append(f"  {name}_config:")
    o.append(f"  {name}_data:")
    o.append("")
    o.append("networks:")
    o.append("  default:")
    o.append(f"    name: {name}_net")
    o.append("    driver: overlay")
    o.append("    attachable: true")
    o.append("")
    return "\n".join(o)
