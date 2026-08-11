#!/usr/bin/env python3
"""Apply the authoritative desc_map to:
  1. each folder's README.md  (create if missing, using full template)
  2. the commented homepage.description line in docker-compose.yml AND swarm/docker-stack.yml
"""
import os, re, json

ROOT = "/home/bfoleylv/Desktop/selfhosted done"
SKIP = {"AUDIT-REPORT.txt", "README.md", ".tools", ".git"}
desc_map = json.load(open("/tmp/desc_map.json"))

dirs = sorted([d for d in os.listdir(ROOT)
               if os.path.isdir(os.path.join(ROOT, d)) and d not in SKIP])

def parse_compose(path):
    img=port=cat=hc="TCP port probe"
    try: txt=open(path).read()
    except: return dict(image=None,port=None)
    m=re.search(r'image:\s*([^\s#]+)', txt)
    if m: img=m.group(1).strip().strip('"\'')
    pm=re.search(r'-\s*"?(\d+):\d+', txt)
    if pm: port=pm.group(1)
    mc=re.search(r'\*\*Category\*\*\s*\|\s*(.+)', txt)
    return dict(image=img, port=port)

def prettify(name):
    fixes={"mysql-mariadb":"MySQL / MariaDB","airsonic-advanced":"Airsonic Advanced",
           "bitwarden-rs":"Bitwarden RS (Vaultwarden)","vault-warden":"Vaultwarden",
           "elastic-search":"Elasticsearch","cockroachdb":"CockroachDB",
           "opensearch":"OpenSearch","paperless-ngx":"Paperless-ngx",
           "uptime-kuma":"Uptime Kuma","nginx-proxy-manager":"Nginx Proxy Manager",
           "gitea":"Gitea","searxng":"SearXNG"}
    if name in fixes: return fixes[name]
    return name.replace("-"," ").replace("_"," ").title()

def write_readme(d, desc):
    p=os.path.join(ROOT,d,"README.md")
    c=parse_compose(os.path.join(ROOT,d,"docker-compose.yml"))
    img=c["image"] or "—"
    port=c["port"] or "—"
    title=prettify(d)
    body=(f"# {title}\n\n"
          f"{desc}\n\n"
          f"| | |\n|---|---|\n"
          f"| **Image** | `{img}` |\n"
          f"| **Host port** | `{port}` |\n"
          f"| **Container port** | `{port}` |\n"
          f"| **Category** | Self Hosting Solutions |\n"
          f"| **Healthcheck** | TCP port probe |\n\n"
          f"## Run it\n\nSingle host:\n\n```bash\ndocker compose up -d\n```\n\n"
          f"Then open <http://localhost:{port}>.\n\nSwarm:\n\n"
          f"```bash\ndocker stack deploy -c swarm/docker-stack.yml {d}\n```\n\n"
          f"## Layout\n\n```\ndocker-compose.yml        # single-host deployment\n"
          f"swarm/docker-stack.yml    # swarm stack (named volumes, replicas, placement)\n"
          f"config/                   # mounted to /config\ndata/                     # mounted to /data\n```\n\n"
          f"## Check it is healthy\n\n```bash\ndocker inspect --format '{{.State.Health.Status}}' {d}\n```\n\n"
          f"## Homepage\n\n[gethomepage](https://github.com/gethomepage/homepage) labels are included but "
          f"commented out. Uncomment the `labels:` block in `docker-compose.yml` to enable autodiscovery.\n")
    open(p,"w").write(body)
    return True

n_readme=0; n_hp=0
for d in dirs:
    entry=desc_map.get(d)
    if not entry: continue
    desc=entry["desc"].rstrip(".")
    # 1) folder README (create or update)
    p=os.path.join(ROOT,d,"README.md")
    if os.path.exists(p):
        lines=open(p).read().split("\n")
        for i,ln in enumerate(lines):
            st=ln.strip()
            if st and not st.startswith("#"):
                lines[i]=desc; break
        open(p,"w").write("\n".join(lines))
    else:
        write_readme(d, desc)
    n_readme+=1
    # 2) homepage.description
    for f in ("docker-compose.yml","swarm/docker-stack.yml"):
        fp=os.path.join(ROOT,d,f)
        if not os.path.exists(fp): continue
        txt=open(fp).read()
        new,n2=re.subn(r'(#\s*-\s*"homepage\.description=)[^"\n]*',
                       lambda m: m.group(1)+desc+'.', txt)
        if n2:
            open(fp,"w").write(new); n_hp+=n2

print("folder READMEs written/updated:",n_readme)
print("homepage.description lines updated:",n_hp)
