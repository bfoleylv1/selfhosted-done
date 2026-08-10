# selfhosted-done

A library of **545** Docker Compose + Docker Swarm stacks for self-hosted services. Each folder contains a working `docker-compose.yml` (single host) and `swarm/docker-stack.yml` (cluster), with healthchecks, Homepage labels, and config/data volume mounts.

Every stack was generated from the project's real upstream image and tagged with its actual category and host port. Descriptions come from each project's official catalog/repo where available, and a clean short summary for every service.

## At a glance

- **Services:** 545
- **With GPU / hardware-acceleration blocks:** 50 (commented out — uncomment to enable)
- **Categories:** 34
- **Layout per service:** `docker-compose.yml`, `swarm/docker-stack.yml`, `config/`, `data/`
- **Each folder also has its own `README.md`** with image, ports, category, and run command.

## How to run

Single host:

```bash
cd <service>
docker compose up -d
```

Swarm:

```bash
docker stack deploy -c <service>/swarm/docker-stack.yml <service>
```

> Healthchecks are enabled but the `homepage.*` labels are commented out so they don't clutter a Homepage instance you don't have. Uncomment them in each compose to populate Homepage.

## Services by category

### Self Hosting Solutions (217)

| Service | Image | Port | GPU | Description |
|---|---|---|:--:|---|
| [42Links](./42links) | `node:20-alpine` | `8080` | — | Self-hosted bookmark and link dashboard |
| [92Five](./92five) | `php:8.2-apache` | `20393` | — | Self-hosted project management and collaboration tool |
| [Adyen Proxy](./adyen-proxy) | `node:20-alpine` | `20396` | — | Reverse proxy / bridge for the Adyen payment API |
| [Agent Vault](./agent-vault) | `hashicorp/vault:latest` | `20398` | — | Open-source HTTP credential proxy and vault that brokers API credentials for AI agents without exposing the secrets |
| [Akkoma](./akkoma) | `akkoma/akkoma:latest` | `20400` | — | Lightweight federated microblogging server (ActivityPub, Mastodon-compatible) |
| [Alfresco](./alfresco) | `alfresco/alfresco-content-repository-community:latest` | `20408` | — | Alfresco self-hosted service. |
| [Aliasvault](./aliasvault) | `ghcr.io/aliasvault/aliasvault:latest` | `20409` | — | Aliasvault self-hosted service. |
| [Answer](./answer) | `answerdev/answer:latest` | `20411` | — | Answer self-hosted service. |
| [Anythingllm](./anythingllm) | `mintplexlabs/anythingllm:latest` | `20412` | ✅ | Anythingllm self-hosted service. |
| [Appwrite](./appwrite) | `appwrite/appwrite:1.6.0` | `20003` | — | Open-source backend-as-a-service (BaaS) for web and mobile apps |
| [Archivebox](./archivebox) | `ghcr.io/archivebox/archivebox:latest` | `20413` | — | Archivebox self-hosted service. |
| [B1Gmail](./b1gMail) | `php:8.2-apache` | `20006` | — | Self-hosted webmail and mail server suite |
| [Baikal](./baikal) | `ckulka/baikal:nginx` | `20009` | — | Lightweight CalDAV and CardDAV server |
| [Bamboo](./bamboo) | `atlassian/bamboo:latest` | `8085` | — | Atlassian continuous integration and deployment server (commercial) |
| [Bar Assistant](./bar-assistant) | `barassistant/server:v5` | `20010` | — | Self-hosted cocktail and drink recipe manager |
| [Booklore](./booklore) | `ghcr.io/booklore-app/booklore:latest` | `6060` | — | Self-hosted book library and reading tracker |
| [Browserstack Turboscale](./browserstack-turboscale) | `alpine:3.20` | `20019` | — | BrowserStack TurboScale - self-hosted device testing infrastructure (commercial) |
| [Buddy Enterprise](./buddy-enterprise) | `debian:12-slim` | `20020` | — | Buddy Enterprise - self-hosted CI/CD automation server (commercial) |
| [Bumpress](./bumpress) | `wordpress:latest` | `20419` | — | Bumpress self-hosted service. |
| [C15T](./c15t) | `node:20-alpine` | `20021` | — | Open-source consent and privacy management platform |
| [Calibre](./calibre) | `linuxserver/calibre:latest` | `8083` | — | Calibre self-hosted service. |
| [Canvas Lms](./canvas-lms) | `instructure/canvas-lms:stable` | `3000` | — | Open-source learning management system (LMS) |
| [Cap](./cap) | `alpine:3.20` | `20023` | — | Open-source screen recording and sharing tool |
| [Castopod](./castopod) | `castopod/castopod:latest` | `20024` | ✅ | Self-hosted podcast hosting platform with ActivityPub federation |
| [Centrifugo](./centrifugo) | `centrifugo/centrifugo:v5` | `20025` | — | Real-time messaging server (WebSocket/SSE) for live updates |
| [Cerbos](./cerbos) | `ghcr.io/cerbos/cerbos:latest` | `3592` | — | Open-source fine-grained authorization / access-control engine |
| [Cgit](./cgit) | `alpine:3.20` | `20027` | — | Lightweight web frontend for Git repositories |
| [Changedetection](./changedetection) | `dgtlmoon/changedetection.io:latest` | `20422` | — | Changedetection self-hosted service. |
| [Claude Code](./claude-code) | `anthropics/claude-code:latest` | `20530` | — | Claude Code self-hosted service. |
| [Cloudron](./cloudron) | `ubuntu:24.04` | `20033` | — | Self-hosted PaaS for installing and managing web apps |
| [Cluster Control](./cluster-control) | `severalnines/clustercontrol:latest` | `20034` | — | Severalnines ClusterControl - database cluster management and monitoring |
| [Cockpit](./cockpit) | `quay.io/cockpit/ws:latest` | `9090` | — | Web-based Linux server administration dashboard |
| [Collabora Online](./collabora-online) | `collabora/code:latest` | `9980` | — | Self-hosted LibreOffice-based online office suite |
| [Comfyui](./comfyui) | `ghcr.io/ai-dock/comfyui:latest` | `8188` | ✅ | Node-based graphical UI for Stable Diffusion / generative AI |
| [Commentario](./commentario) | `registry.gitlab.com/comentario/comentario:latest` | `20036` | — | Self-hosted comment system for static sites |
| [Conduit](./conduit) | `matrixconduit/matrix-conduit:latest` | `6167` | — | Lightweight Matrix homeserver written in Rust |
| [Crucial](./crucial) | `alpine:3.20` | `20038` | — | Self-hosted service. |
| [Daisy](./daisy) | `alpine:3.20` | `20040` | — | Self-hosted service. |
| [Datasette](./datasette) | `datasetteproject/datasette:latest` | `8001` | — | Explore and publish SQLite databases as JSON APIs and dashboards |
| [Davical](./davical) | `php:8.2-apache` | `20041` | — | CalDAV server for calendar sharing |
| [Davis](./davis) | `ghcr.io/tchapi/davis:latest` | `20042` | — | Self-hosted CalDAV/CardDAV server (PHP) |
| [Debops](./debops) | `debops/debops:latest` | `20434` | — | Debops self-hosted service. |
| [Depay](./depay) | `node:20-alpine` | `20043` | — | Self-hosted crypto payment processor |
| [Dify](./dify) | `langgenius/dify-api:latest` | `20531` | ✅ | Dify self-hosted service. |
| [Discourse](./discourse) | `discourse/discourse:latest` | `20436` | — | Discourse self-hosted service. |
| [Docuddle](./docuddle) | `alpine:3.20` | `20046` | — | Self-hosted service. |
| [Documenso](./documenso) | `documenso/documenso:latest` | `20047` | — | Open-source DocuSign alternative for electronic signatures |
| [Dpaste](./dpaste) | `python:3.11-slim` | `20050` | — | Self-hosted pastebin / code snippet service |
| [Dreamfactory](./dreamfactory) | `dreamfactorysoftware/df-docker:latest` | `20051` | — | Auto-generated REST API backend for databases |
| [Druid](./druid) | `apache/druid:31.0.0` | `20053` | — | Real-time analytics database (OLAP) |
| [Duckduckgo Proxy](./duckduckgo-proxy) | `benbusby/whoogle-search:latest` | `5000` | — | Self-hosted proxy for the DuckDuckGo search API |
| [Easypanel](./easypanel) | `easypanel/easypanel:latest` | `20056` | — | Modern self-hosted PaaS control panel for Docker apps |
| [Ejabberd](./ejabberd) | `ejabberd/ecs:latest` | `5280` | — | Robust XMPP / Jabber messaging server |
| [Ekso](./ekso) | `alpine:3.20` | `20057` | — | Self-hosted service. |
| [Element](./element) | `vectorim/element-web:latest` | `20438` | — | Element self-hosted service. |
| [Element Web](./element-web) | `vectorim/element-web:latest` | `20058` | — | Web client for the Matrix decentralized chat protocol |
| [Element Web App](./element-web-app) | `vectorim/element-web:latest` | `20059` | — | Matrix client for secure decentralized communication. |
| [Elixire](./elixire) | `alpine:3.20` | `20060` | — | Self-hosted file hosting service |
| [Emqx](./emqx) | `emqx/emqx:latest` | `18083` | — | Scalable open-source MQTT broker for IoT |
| [Enclosed](./enclosed) | `ghcr.io/corentinth/enclosed:latest` | `8787` | — | Self-hosted tool for sharing secrets and files securely |
| [Engity Bifrost](./engity-bifrost) | `alpine:3.20` | `20061` | — | Engity Bifrost - identity and SSO gateway |
| [Epicyon](./epicyon) | `python:3.11-slim` | `20062` | — | Self-hosted ActivityPub federated social server |
| [Ergo](./ergo) | `ergochat/ergo:latest` | `20441` | — | Ergo self-hosted service. |
| [Excalidraw](./excalidraw) | `excalidraw/excalidraw:latest` | `20064` | — | Virtual whiteboard for hand-drawn diagrams |
| [Fmd Server](./fmd-server) | `golang:1.23-alpine` | `20071` | — | Self-hosted service. |
| [Formio](./formio) | `formio/formio:latest` | `3001` | — | Form and API platform for building data-driven forms and apps |
| [Forward Email](./forward-email) | `node:20-alpine` | `20074` | — | Open-source email forwarding and alias service |
| [Framadate](./framadate) | `php:8.2-apache` | `20076` | — | Self-hosted poll and meeting-scheduling tool |
| [Fredy](./fredy) | `ghcr.io/orangecoding/fredy:latest` | `9998` | — | Self-hosted price comparison and shopping tool |
| [Freepbx](./freepbx) | `debian:12-slim` | `20077` | — | Web-based open-source PBX built on Asterisk |
| [Freeswitch](./freeswitch) | `safarov/freeswitch:latest` | `20078` | — | Open-source telephony platform / softswitch (VoIP) |
| [Frigate](./frigate) | `ghcr.io/blakeblackshear/frigate:stable` | `20081` | ✅ | AI-powered network video recorder (NVR) for camera streams |
| [Full Help](./full-help) | `alpine:3.20` | `20083` | — | Self-hosted service. |
| [Fusio](./fusio) | `fusio/fusio:latest` | `20085` | — | Open-source API management platform |
| [Gamevault](./gamevault) | `phalcode/gamevault-backend:latest` | `20086` | — | Self-hosted video game library manager |
| [Garagehq](./garagehq) | `dxflrs/garage:v1.0.1` | `3900` | — | Lightweight S3-compatible distributed object storage |
| [Gaseous Server](./gaseous-server) | `gaseousgames/gaseousserver:latest` | `5198` | — | Self-hosted video game collection / ROM manager |
| [Gathio](./gathio) | `ghcr.io/lowercasename/gathio:latest` | `20087` | — | Self-hosted event page and RSVP host |
| [Geo2Tz](./geo2tz) | `noandrea/geo2tz:latest` | `20088` | — | Convert geographic coordinates to a timezone |
| [Ghostery](./ghostery) | `alpine:3.20` | `20089` | — | Privacy / tracker-blocking browser extension (commercial) |
| [Github Ntfy](./github-ntfy) | `binwiederhier/ntfy:latest` | `20091` | — | ntfy push notifications for GitHub events |
| [Github Runner](./github-runner) | `myoung34/github-runner:latest` | `20092` | — | Self-hosted GitHub Actions runner |
| [Glance](./glance) | `glanceapp/glance:latest` | `20094` | — | Self-hosted dashboard for your homelab and services |
| [Glitchtip](./glitchtip) | `glitchtip/glitchtip:latest` | `20095` | — | Open-source error tracking (Sentry alternative) |
| [Globaleaks](./globaleaks) | `globaleaks/globaleaks:latest` | `20096` | — | Open-source whistleblowing / secure submission platform |
| [Go Feature Flag](./go-feature-flag) | `thomaspoignant/go-feature-flag:latest` | `1031` | — | Feature flag management system (Go) |
| [Gomodel](./gomodel) | `golang:1.23-alpine` | `20099` | — | GoModel: open-source AI gateway / control plane proxy with an OpenAI- and Anthropic-compatible API (a LiteLLM alternative). — [site](https://github.com/ENTERPILOT/GoModel) |
| [Google Cse Proxy](./google-cse-proxy) | `node:20-alpine` | `20100` | — | Proxy for the Google Custom Search Engine API |
| [Gordian](./gordian) | `alpine:3.20` | `20101` | — | Self-hosted service. |
| [Gotify](./gotify) | `gotify/server:latest` | `20448` | — | Gotify self-hosted service. |
| [Habitica](./habitica) | `habitica/habitica:latest` | `20451` | — | Habitica self-hosted service. |
| [Halo](./halo) | `halohub/halo:latest` | `20452` | — | Halo self-hosted service. |
| [Homeassistant](./homeassistant) | `ghcr.io/home-assistant/home-assistant:stable` | `20455` | — | Homeassistant self-hosted service. |
| [Homer](./homer) | `b4bz/homer:latest` | `20112` | — | Static dashboard / startpage for your homelab |
| [Hoppscotch](./hoppscotch) | `hoppscotch/hoppscotch:latest` | `20456` | — | Hoppscotch self-hosted service. |
| [Immich](./immich) | `ghcr.io/immich-app/immich-server:release` | `2283` | ✅ | Immich self-hosted service. |
| [Jellyfin Library](./jellyfin-library) | `jellyfin/jellyfin:latest` | `20118` | — | Tool for managing Jellyfin media libraries |
| [Kanboard](./kanboard) | `kanboard/kanboard:latest` | `20121` | — | Simple kanban board for project management |
| [Langflow](./langflow) | `langflowai/langflow:latest` | `20463` | ✅ | Langflow self-hosted service. |
| [Libervrt](./libervrt) | `lscr.io/linuxserver/emby:latest` | `20139` | — | Self-hosted service. |
| [Librechat](./librechat) | `librechat/librechat:latest` | `20465` | — | Librechat self-hosted service. |
| [Litellm](./litellm) | `ghcr.io/berriai/litellm:main-latest` | `4000` | ✅ | Proxy gateway for 100+ LLM providers with load balancing and fallbacks |
| [Lms](./lms) | `lmscommunity/lyrionmusicserver:latest` | `20142` | — | Frappe LMS: 100% open-source learning management system. — [site](https://github.com/frappe/lms) |
| [Lobechat](./lobechat) | `lobehub/lobe-chat:latest` | `20469` | — | Lobechat self-hosted service. |
| [Lxd](./lxd) | `ubuntu:24.04` | `20144` | ✅ | System container and virtual machine manager (LXC) |
| [Metabase](./metabase) | `metabase/metabase:latest` | `20553` | — | Metabase self-hosted service. |
| [Metube](./metube) | `alexta69/metube:latest` | `20475` | — | Metube self-hosted service. |
| [Mindsdb](./mindsdb) | `mindsdb/mindsdb:latest` | `20476` | — | Mindsdb self-hosted service. |
| [Mollie Proxy](./mollie-proxy) | `node:20-alpine` | `20160` | — | Proxy for the Mollie payment API |
| [Mylar3](./mylar3) | `linuxserver/mylar3:latest` | `20539` | — | Mylar3 self-hosted service. |
| [Netlify](./netlify) | `node:20-alpine` | `20162` | — | Platform for deploying static / Jamstack sites (open-core) |
| [Nextchat](./nextchat) | `yidadaa/chatgpt-next-web:latest` | `20164` | — | Next-generation web UI for ChatGPT and other LLMs |
| [Notion Clone](./notion-clone) | `appflowyinc/appflowy_cloud:latest` | `20170` | — | Open-source Notion alternative for note-taking |
| [Online Invoicing](./online-invoicing) | `php:8.2-apache` | `20173` | — | Self-hosted invoicing / billing tool |
| [Openclaw](./openclaw) | `ghcr.io/openclaw/openclaw:latest` | `20175` | — | OpenClaw: self-hosted personal AI assistant (cross-platform). — [site](https://github.com/openclaw/openclaw) |
| [Opencode](./opencode) | `node:20-alpine` | `20176` | — | Open-source AI coding agent / assistant |
| [Organizr](./organizr) | `organizr/organizr:latest` | `20185` | — | Organize your homelab tabs into a single login dashboard |
| [Para](./para) | `eclipse-temurin:17-jre` | `20190` | — | Flexible open-source backend framework / object storage |
| [Paypal Proxy](./paypal-proxy) | `node:20-alpine` | `20196` | — | Proxy for the PayPal payment API |
| [Pgdog](./pgdog) | `ghcr.io/pgdogdev/pgdog:latest` | `20200` | — | PostgreSQL connection pooler and proxy |
| [Phice](./phice) | `alpine:3.20` | `20201` | — | Self-hosted service. |
| [Phorge](./phorge) | `php:8.2-apache` | `20202` | — | Open-source project management and collaboration platform (Phabricator fork) |
| [Piefed](./piefed) | `python:3.11-slim` | `20204` | — | Federated feed aggregator (ActivityPub) |
| [Plausible](./plausible) | `ghcr.io/plausible/community-edition:v2.1.4` | `20208` | — | Privacy-friendly, open-source web analytics |
| [Plunker](./plunker) | `node:20-alpine` | `20211` | — | Online code editor / playground for web development |
| [Pocket Id](./pocket-id) | `ghcr.io/pocket-id/pocket-id:latest` | `1411` | — | Simple SSO identity provider with passkey support |
| [Pocketbase](./pocketbase) | `ghcr.io/muchobien/pocketbase:latest` | `8090` | — | Open-source backend (SQLite + realtime + auth) in a single file |
| [Portainer](./portainer) | `portainer/portainer-ce:latest` | `9443` | — | Lightweight web UI for managing Docker, Swarm and Kubernetes |
| [Postal](./postal) | `ghcr.io/postalserver/postal:latest` | `20214` | — | Full-featured open-source mail server |
| [Poste Io](./poste-io) | `analogic/poste.io:latest` | `20215` | — | Self-hosted mail server suite (SMTP/IMAP/POP) |
| [Proxmox](./proxmox) | `ubuntu:24.04` | `20222` | ✅ | Open-source server virtualization platform (Proxmox VE) |
| [Pushbits](./pushbits) | `ghcr.io/pushbits/server:latest` | `20225` | — | Self-hosted push notification relay for Android/iOS |
| [R2](./r2) | `minio/minio:latest` | `20229` | — | Self-hosted proxy for Cloudflare R2 object storage |
| [Radicale](./radicale) | `tomsquest/docker-radicale:latest` | `5232` | — | Simple CalDAV and CardDAV server |
| [Redirect](./redirect) | `alpine:3.20` | `20238` | — | Simple HTTP redirect / URL-forwarding service |
| [Repo Flow](./repo-flow) | `alpine:3.20` | `20240` | — | Self-hosted service. |
| [Reservo](./reservo) | `reservo/reservo:latest` | `20241` | — | Self-hosted image hosting and sharing script |
| [Resourcespace](./resourcespace) | `php:8.2-apache` | `20242` | — | Open-source digital asset management (DAM) |
| [Restreamer](./restreamer) | `datarhei/restreamer:latest` | `20244` | ✅ | Live video streaming server (RTSP/RTMP restreaming) |
| [Revent](./revent) | `alpine:3.20` | `20246` | — | Self-hosted service. |
| [Revert](./revert) | `node:20-alpine` | `20247` | — | Self-hosted service. |
| [Rgit](./rgit) | `alpine:3.20` | `20248` | — | Self-hosted Git repository manager / viewer |
| [Rhode Code](./rhode-code) | `python:3.11-slim` | `20249` | — | Source code management platform (Git/Mercurial/SVN) |
| [Routr](./routr) | `fonoster/routr:latest` | `20252` | — | SIP server for VoIP and telephony routing |
| [Rs Short](./rs-short) | `alpine:3.20` | `20254` | — | Self-hosted URL shortener |
| [Rss Bridge](./rss-bridge) | `rssbridge/rss-bridge:latest` | `20256` | — | Generate RSS feeds for websites that don't provide them |
| [Rudderstack](./rudderstack) | `rudderlabs/rudder-server:latest` | `20258` | — | Open-source customer data platform (CDP) |
| [Rukovoditel](./rukovoditel) | `php:8.2-apache` | `20259` | — | Free web-based project management and CRM |
| [Sabre Dav](./sabre-dav) | `php:8.2-apache` | `20260` | — | WebDAV, CalDAV and CardDAV server library/framework |
| [Salut A Toi](./salut-a-toi) | `alpine:3.20` | `20263` | — | Multipurpose XMPP/Jabber client and ecosystem |
| [Sama](./sama) | `alpine:3.20` | `20264` | — | SAMA: next-gen self-hosted chat server and clients (GPL-3.0, Node.js/Docker) |
| [Seaweedfs](./seaweedfs) | `chrislusf/seaweedfs:latest` | `9333` | — | Distributed object, block and file storage system |
| [Sendy](./sendy) | `php:8.2-apache` | `20271` | — | Self-hosted email marketing platform (Amazon SES based) |
| [Seppo](./seppo) | `alpine:3.20` | `20273` | — | Self-hosted service. |
| [Shkeeper](./shkeeper) | `python:3.11-slim` | `20277` | — | Self-hosted crypto payment gateway |
| [Signoz](./signoz) | `signoz/query-service:latest` | `20281` | — | Open-source observability platform (traces, metrics, logs) |
| [Sip3](./sip3) | `alpine:3.20` | `20282` | — | VoIP / SIP monitoring and analysis |
| [Smederee](./smederee) | `alpine:3.20` | `20284` | — | Smederee: a frugal platform for building software together, leveraging the Darcs version control system (AGPL-3.0) |
| [Smite](./smite) | `alpine:3.20` | `20285` | — | Self-hosted service. |
| [Snypy](./snypy) | `python:3.11-slim` | `20288` | — | Self-hosted code snippet manager |
| [Socks5 Proxy Server](./socks5-proxy-server) | `serjs/go-socks5-proxy:latest` | `1080` | — | Self-hosted SOCKS5 proxy server |
| [Speed Test](./speed-test) | `openspeedtest/latest:latest` | `20291` | — | Self-hosted network speed-test server |
| [Spoolman](./spoolman) | `ghcr.io/donkie/spoolman:latest` | `20293` | — | Filament and spool inventory manager for 3D printing |
| [Squidex](./squidex) | `squidex/squidex:latest` | `20296` | — | Open-source headless CMS |
| [Srs](./srs) | `ossrs/srs:5` | `1985` | ✅ | Simple, high-performance RTMP/WebRTC streaming server |
| [Stack Auth](./stack-auth) | `node:20-alpine` | `20298` | — | Open-source authentication and user management |
| [Stalwart Mail](./stalwart-mail) | `stalwartlabs/stalwart:latest` | `20299` | — | All-in-one mail server (SMTP/IMAP/JMAP) written in Rust |
| [Stirling Pdf](./stirling-pdf) | `ghcr.io/stirling-tools/stirling-pdf:latest` | `20302` | — | Local PDF manipulation toolkit (merge, split, convert) |
| [Stripe Proxy](./stripe-proxy) | `node:20-alpine` | `20307` | — | Proxy for the Stripe payment API |
| [Stripe Self Hosted](./stripe-self-hosted) | `node:20-alpine` | `20308` | — | Self-hosted Stripe integration / API proxy |
| [Subtitle Converter](./subtitle-converter) | `lscr.io/linuxserver/ffmpeg:latest` | `20309` | — | Convert and translate subtitle file formats |
| [Supers3Cret](./supers3cret) | `alpine:3.20` | `20311` | — | Self-hosted service. |
| [Supportpal](./supportpal) | `php:8.2-apache` | `20312` | — | Self-hosted helpdesk / support desk software (commercial) |
| [Surfer](./surfer) | `node:20-alpine` | `20313` | — | Static file hosting and web publishing tool (Cloudron Surfer) |
| [Surge](./surge) | `node:20-alpine` | `20314` | — | Self-hosted service. |
| [Svix](./svix) | `svix/svix-server:latest` | `8071` | — | Open-source webhook service and infrastructure |
| [Synapse](./synapse) | `matrixdotorg/synapse:latest` | `20318` | — | Reference Matrix homeserver for federated chat |
| [Teikei](./teikei) | `node:20-alpine` | `20320` | — | Self-hosted service. |
| [Telebugs](./telebugs) | `ruby:3.3-alpine` | `20321` | — | Self-hosted bug and error tracking service |
| [Text Gen Inference](./text-gen-inference) | `ghcr.io/huggingface/text-generation-inference:latest` | `20323` | — | Text generation inference server for LLMs (HuggingFace TGI) |
| [Thelia](./thelia) | `php:8.2-apache` | `20325` | — | Open-source e-commerce platform (PHP) |
| [Thumbor](./thumbor) | `ghcr.io/thumbor/thumbor:latest` | `20326` | — | On-the-fly image thumbnail and resize service |
| [Tigase](./tigase) | `tigase/tigase-xmpp-server:latest` | `20327` | — | High-performance XMPP / Jabber server |
| [Tileserver Gl](./tileserver-gl) | `maptiler/tileserver-gl:latest` | `20328` | — | Serve vector and raster map tiles (Mapbox GL) |
| [Tinode](./tinode) | `tinode/tinode:latest` | `20330` | — | Instant messaging server with REST and websocket APIs |
| [Trailbase](./trailbase) | `trailbase/trailbase:latest` | `20333` | — | Open-source backend (auth + DB + API) written in Rust |
| [Trigger Dev](./trigger-dev) | `ghcr.io/triggerdotdev/trigger.dev:v3` | `20334` | — | Open-source background jobs and workflow engine |
| [Tuleap](./tuleap) | `tuleap/tuleap-community-edition:latest` | `20336` | — | Open-source ALM and project management (Agile + DevOps) |
| [Tuwunel](./tuwunel) | `ghcr.io/matrix-construct/tuwunel:latest` | `20338` | — | Matrix homeserver written in Rust |
| [Txtdot](./txtdot) | `node:20-alpine` | `20339` | — | txtdot: HTTP proxy that strips pages down to text, links and images to save bandwidth and block ads/scripts. — [site](https://github.com/TempoWorks/txtdot) |
| [Url To Png](./url-to-png) | `ghcr.io/browserless/chromium:latest` | `20345` | — | Render URLs to PNG screenshots |
| [Vercel](./vercel) | `node:20-alpine` | `20348` | — | Platform for frontend deployment (open-core) |
| [Wagmios](./wagmios) | `alpine:3.20` | `20352` | — | Wagmios: give your AI agent a homelab (self-hosted agent tooling). — [site](https://github.com/mentholmike/wagmios) |
| [Wakapi](./wakapi) | `ghcr.io/muety/wakapi:latest` | `20353` | — | Self-hosted coding time and activity tracker (WakaTime compatible) |
| [Watchcode](./watchcode) | `alpine:3.20` | `20355` | — | Self-hosted service. |
| [Watchtower](./watchtower) | `containrrr/watchtower:latest` | `20356` | — | Automatically update Docker containers to the latest images |
| [Wazo](./wazo) | `debian:12-slim` | `20357` | — | Open-source IP-PBX telephony platform |
| [Webiny](./webiny) | `node:20-alpine` | `20360` | — | Open-source serverless CMS and application framework |
| [Wikipedia Kiwix](./wikipedia-kiwix) | `ghcr.io/kiwix/kiwix-serve:latest` | `20364` | — | Offline Wikipedia mirror; search Wikimedia projects without internet. |
| [Wildduck](./wildduck) | `nodemailer/wildduck:latest` | `20365` | — | IMAP/POP3 mail server written in Node.js |
| [Wireguard Vpn](./wireguard-vpn) | `lscr.io/linuxserver/wireguard:latest` | `20366` | — | Fast modern VPN using the WireGuard protocol |
| [Workadventure](./workadventure) | `thecodingmachine/workadventure-play:master` | `20370` | — | Collaborative virtual office / worlds (MMORPG-style) |
| [Xandikos](./xandikos) | `ghcr.io/jelmer/xandikos:latest` | `20372` | — | CalDAV server written in Python |
| [Xcpg](./xcpg) | `ubuntu:24.04` | `20373` | ✅ | Self-hosted service. |
| [Yarn Social](./yarn-social) | `prologic/yarnd:latest` | `20375` | — | Self-hosted microblog (Yarn.social, Gemtext-based) |
| [Ydl Api Ng](./ydl-api-ng) | `python:3.11-slim` | `20376` | — | REST API wrapper for youtube-dl / yt-dlp downloads |
| [Yeti Switch](./yeti-switch) | `alpine:3.20` | `20377` | — | Yeti Switch - softswitch / SBC for VoIP |
| [Yetishare](./yetishare) | `php:8.2-apache` | `20378` | — | Self-hosted file hosting and sharing script |
| [Yourls](./yourls) | `yourls:latest` | `20379` | — | Self-hosted URL shortener |
| [Youtubedl Server](./youtubedl-server) | `nbr23/youtube-dl-server:latest` | `20380` | — | Web UI for youtube-dl downloads |
| [Yt Dlp Web Ui](./yt-dlp-web-ui) | `marcobaobao/yt-dlp-webui:latest` | `3033` | — | Web UI for yt-dlp video downloads |
| [Zed](./zed) | `alpine:3.20` | `20381` | — | High-performance multiplayer code editor (server component) |
| [Zeit](./zeit) | `node:20-alpine` | `20383` | — | Self-hosted service. |
| [Zimbra Collaboration](./zimbra-collaboration) | `ubuntu:24.04` | `20387` | — | Open-source email and collaboration suite |
| [Zincsearch](./zincsearch) | `public.ecr.aws/zinclabs/zincsearch:latest` | `4080` | — | Lightweight search engine (Elasticsearch alternative) |
| [Zk Cloudserver](./zk-cloudserver) | `alpine:3.20` | `20388` | — | Self-hosted service. |
| [Zot Oci Registry](./zot-oci-registry) | `ghcr.io/project-zot/zot-linux-amd64:latest` | `20390` | — | OCI container image registry (Zot) |

### Analytics (17)

| Service | Image | Port | GPU | Description |
|---|---|---|:--:|---|
| [Ackee](./ackee) | `electerious/ackee:latest` | `20394` | — | Lightweight anonymised web analytics; self-hosted solution. |
| [Awstats](./awstats) | `php:8.2-apache` | `20004` | — | Advanced web statistics; detailed reporting and log analysis. |
| [Chronograf](./chronograf) | `chronograf:latest` | `20028` | — | Admin UI for InfluxDB; manage databases and monitoring. |
| [Goaccess](./goaccess) | `allinurl/goaccess:latest` | `7890` | — | Real-time web log analyzer; interactive HTML reports. |
| [Grafana](./grafana) | `grafana/grafana:latest` | `20104` | — | Analytics and monitoring visualization platform; Grafana dashboards. |
| [Graphite](./graphite) | `graphiteapp/graphite-statsd:latest` | `20105` | — | Enterprise monitoring and time-series database; monitoring graphs. |
| [Icehound](./icehound) | `alpine:3.20` | `20115` | — | AI-powered tool for incident response and system monitoring. |
| [Kapacitor](./kapacitor) | `kapacitor:latest` | `9092` | — | Data process and monitoring application; TICK stack component. |
| [Logstash](./logstash) | `docker.elastic.co/logstash/logstash:8.15.0` | `9600` | — | Data processing pipeline; collect, transform, and forward data. |
| [Loki](./loki) | `grafana/loki:latest` | `3100` | — | Log aggregation system; designed to be cost-effective and easily run. |
| [Matomo](./matomo) | `matomo:latest` | `20152` | — | Open-source web analytics platform; full control over your data. |
| [Openwebui](./openwebui) | `ghcr.io/open-webui/open-webui:main` | `20184` | ✅ | Self-hosted OpenAI-powered web UI; chat with AI models locally. |
| [Plausible Analytics](./plausible-analytics) | `ghcr.io/plausible/community-edition:v2.1.4` | `20209` | — | Simple, privacy-focused web analytics alternative to Google Analytics. |
| [Prometheus](./prometheus) | `prom/prometheus:latest` | `20221` | — | Monitoring and alerting toolkit; systems and services monitoring. |
| [Sentry](./sentry) | `sentry:latest` | `20272` | — | Open-source error tracking tool; monitor and improve software |
| [Tempo](./tempo) | `grafana/tempo:latest` | `3200` | — | Distributed tracing platform; end-to-end telemetry collection. |
| [Umami](./umami) | `ghcr.io/umami-software/umami:postgresql-latest` | `20342` | — | Open-source alternative to Google Analytics; privacy-focused. |

### Crm (17)

| Service | Image | Port | GPU | Description |
|---|---|---|:--:|---|
| [Client Management](./client-management) | `php:8.2-apache` | `20030` | — | Invoice, quotes, and client management for freelancers and agencies. |
| [Dolibarr](./dolibarr) | `dolibarr/dolibarr:latest` | `20048` | — | Web app to manage business activities; ERP/CRM for small companies. |
| [Erpnext](./erpnext) | `frappe/erpnext:latest` | `20063` | — | Open source ERP; built on Frappe framework for business management. |
| [Fossbilling](./fossbilling) | `fossbilling/fossbilling:latest` | `20075` | — | Open source billing and invoicing; replacement for WHMCS. |
| [Magento](./magento) | `alexcheng/magento2:latest` | `20146` | — | Open-source e-commerce platform; Adobe Commerce predecessor. |
| [October Cms](./october-cms) | `php:8.2-apache` | `20171` | — | Content management system; simple and extensible. |
| [Odoo](./odoo) | `odoo:17` | `8069` | — | All-in-one business management suite; CRM, ERP, CMS, and more. |
| [Opencart](./opencart) | `php:8.2-apache` | `20174` | — | Responsive e-commerce solution; ready-to-use online store platform. |
| [Partkeep System](./partkeep-system) | `php:8.2-apache` | `20191` | — | PHP/MySQL web application; organize and manage parts inventory. |
| [Prestashop](./prestashop) | `prestashop/prestashop:latest` | `20218` | — | Free open-source e-commerce solution; customizable online store. |
| [Saleor](./saleor) | `ghcr.io/saleor/saleor:3.20` | `20261` | — | E-commerce platform; GraphQL-first headless commerce solution. |
| [Shopis](./shopis) | `node:20-alpine` | `20278` | — | Admin dashboard for Shopify stores; order and inventory management. |
| [Shopware](./shopware) | `dockware/dev:latest` | `20279` | — | E-commerce platform; open source and enterprise editions available. |
| [Snipe It](./snipe-it) | `snipe/snipe-it:latest` | `20286` | — | Asset management solution; manage your IT assets and equipment. |
| [Spree Commerce](./spree-commerce) | `ruby:3.3-alpine` | `20294` | — | Complete online store platform; Ruby on Rails based. |
| [Sylius](./sylius) | `php:8.2-fpm` | `20317` | — | Symfony-based e-commerce solution; highly customizable. |
| [Woocommerce](./woocommerce) | `wordpress:latest` | `20367` | — | WordPress plugin for e-commerce; highly customizable storefront. |

### Email (17)

| Service | Image | Port | GPU | Description |
|---|---|---|:--:|---|
| [Afterlogic](./afterlogic) | `php:8.2-apache` | `20397` | — | Webmail program; modern webmail with calendar. |
| [Axigen](./axigen) | `axigen/axigen:latest` | `20005` | — | Mail server; enterprise email and collaboration. |
| [Baserow](./baserow) | `baserow/baserow:latest` | `20011` | — | Open source Notion alternative; database and form builder. |
| [Dovecot](./dovecot) | `dovecot/dovecot:latest` | `20049` | — | IMAP and POP3 server; mail delivery and retrieval. |
| [Exim](./exim) | `debian:12-slim` | `20065` | — | Mail transfer agent; configurable message transfer agent. |
| [Iredmail](./iRedMail) | `ubuntu:24.04` | `20114` | — | Complete mail server solution; quick and easy setup. |
| [Mailcow](./mailcow) | `mailcow/rspamd:1.99` | `20147` | — | Email solution; complete mail server suite. |
| [Mailu](./mailu) | `ghcr.io/mailu/admin:2.0` | `20148` | — | Open source email suite; complete mail server stack. |
| [Modoboa](./modoboa) | `python:3.11-slim` | `20159` | — | Mail hosting application; complete mail server suite. |
| [Opensmtpd](./opensmtpd) | `debian:12-slim` | `20182` | — | SMTP server; OpenBSD's mail server. |
| [Postfix](./postfix) | `boky/postfix:latest` | `20216` | — | Mail transfer agent; send and receive email. |
| [Rainloop](./rainloop) | `hardware/rainloop:latest` | `20232` | — | Webmail client; simple and responsive webmail. |
| [Roundcube](./roundcube) | `roundcube/roundcubemail:latest` | `20251` | — | Web-based email client; webmail with plugins. |
| [Sendmail](./sendmail) | `debian:12-slim` | `20270` | — | Most widely used Unix mail transfer agent. |
| [Sogo](./sogo) | `debian:12-slim` | `20000` | — | Web access to IMAP and CalDAV; groupware solution. |
| [Squirrelmail](./squirrelmail) | `php:8.2-apache` | `20297` | — | Web-based email client; traditional webmail interface. |
| [Zimbra](./zimbra) | `ubuntu:24.04` | `20386` | — | Collaboration software; email, calendar, contacts. |

### Productivity (17)

| Service | Image | Port | GPU | Description |
|---|---|---|:--:|---|
| [Appflowy](./appflowy) | `appflowyinc/appflowy_cloud:latest` | `20002` | — | Open source Notion alternative; collaborative workspace builder. |
| [Bookstack](./bookstack) | `lscr.io/linuxserver/bookstack:latest` | `20016` | — | Wiki platform to organize and maintain documentation. |
| [Focalboard](./focalboard) | `mattermost/focalboard:latest` | `20072` | — | Open source Notion alternative; kanban and project management. |
| [Hedgedoc](./hedgedoc) | `quay.io/hedgedoc/hedgedoc:latest` | `20111` | — | Web-based markdown editor for collaborative note-taking. |
| [Joplin](./joplin) | `linuxserver/joplin:latest` | `22300` | — | Note-taking and to-do application; Markdown support with encryption. |
| [Laverna](./laverna) | `alpine:3.20` | `20137` | — | Open source alternative to Evernote; JavaScript-based note app. |
| [Notejot](./notejot) | `alpine:3.20` | `20169` | — | Simple and elegant notes app; lightweight note-taking solution. |
| [Openproject](./openproject) | `openproject/openproject:15` | `20178` | — | Project management web application; issue tracking and agile tools. |
| [Outline](./outline) | `outlinewiki/outline:latest` | `20186` | — | Team knowledge base and documentation; clean and fast wiki. |
| [Plane](./plane) | `makeplane/plane-backend:latest` | `20207` | — | Open source alternative to Notion and Linear; team project management. |
| [Restyaboard](./restyaboard) | `php:8.2-apache` | `20245` | — | Open source Trello alternative; project management and task board. |
| [Standard Notes](./standard-notes) | `standardnotes/server:latest` | `20300` | — | Encrypted notes app; focus on privacy and security. |
| [Taiga](./taiga) | `taigaio/taiga-back:latest` | `20319` | — | Project management tool for Agile development; issue tracking and kanban. |
| [Taskcafe](./taskcafe) | `taskcafe/taskcafe:latest` | `3333` | — | Self-hosted task management; simple and easy to use. |
| [Turtl](./turtl) | `alpine:3.20` | `20337` | — | Open source Evernote alternative; encrypted note-sync platform. |
| [Wekan](./wekan) | `wekanteam/wekan:latest` | `20361` | — | Open source Trello alternative; Kanban-style task management. |
| [Wiki Js](./wiki-js) | `ghcr.io/requarks/wiki:2` | `20363` | — | Modern and powerful wiki app; built on Node.js with Vue.js frontend. |

### Search Engines (16)

| Service | Image | Port | GPU | Description |
|---|---|---|:--:|---|
| [Elasticsearch](./elasticsearch) | `docker.elastic.co/elasticsearch/elasticsearch:8.15.0` | `9200` | ✅ | Distributed search and analytics engine; scalable data store and vector database for production workloads. |
| [Kiwix](./kiwix) | `ghcr.io/kiwix/kiwix-serve:latest` | `20129` | — | Offline Wikipedia reader; hosts ZIM file format for offline browsing. |
| [Library Genesis](./library-genesis) | `nginx:alpine` | `20140` | — | Digital library of books, articles, and academic papers |
| [Meilisearch](./meilisearch) | `getmeili/meilisearch:latest` | `7700` | ✅ | Lightning-fast search engine optimized for apps, websites, and workflows with relevant search experiences. |
| [Metager](./metager) | `php:8.2-fpm` | `20153` | — | German metasearch engine; privacy-focused search results. |
| [OpenSearch](./opensearch) | `opensearchproject/opensearch:latest` | `20180` | — | Fork of Elasticsearch; community-supported search and analytics suite. |
| [Pinecone](./pinecone) | `qdrant/qdrant:latest` | `6333` | — | Fully managed vector database alternative; private cloud deployment available. |
| [Qdrant](./qdrant) | `qdrant/qdrant:latest` | `20227` | ✅ | Fast and privacy-friendly vector search engine with an easy-to-use gRPC API. |
| [SearXNG](./searxng) | `docker.io/searxng/searxng:latest` | `20267` | — | Free and open-source metasearch engine; aggregates results without tracking. |
| [Sefaria](./sefaria) | `python:3.11-slim` | `20268` | — | Digital library of texts; Jewish texts with search and cross-references. |
| [Solr](./solr) | `solr:9` | `8983` | — | Enterprise search platform built on Apache Lucene; powerful full-text search capabilities. |
| [Typesense](./typesense) | `typesense/typesense:27.1` | `8108` | ✅ | Typo-tolerant search engine with fast, relevant results; developer-friendly API. |
| [Weaviate](./weaviate) | `semitechnologies/weaviate:latest` | `20358` | ✅ | GraphQL-native vector database with class-based object storage and search capabilities. |
| [Whoogle](./whoogle) | `benbusby/whoogle-search:latest` | `20362` | — | Google search proxy; minimal Google search in your own server. |
| [Yacy](./yacy) | `yacy/yacy_search_server:latest` | `20374` | — | Decentralized search engine; peer-to-peer indexing and search network. |
| [Zim](./zim) | `ghcr.io/openzim/zim-tools:latest` | `20385` | — | File format for offline Wikipedia and other Wikimedia content. |

### Social (16)

| Service | Image | Port | GPU | Description |
|---|---|---|:--:|---|
| [Bookwyrm](./bookwyrm) | `python:3.11-slim` | `8000` | — | Federated book social network; discover and discuss books. |
| [Crush Propulsion](./crush-propulsion) | `alpine:3.20` | `20039` | — | Social platform for sharing thoughts and ideas. |
| [Friendica](./friendica) | `friendica:latest` | `20080` | — | Decentralized social network; connects to other networks. |
| [Gnuseed](./gnuseed) | `alpine:3.20` | `20097` | — | Distributed social network based on ActivityPub protocol. |
| [Kbin](./kbin) | `php:8.2-fpm` | `20122` | — | Another ActivityPub aggregator; alternative to Lemmy. |
| [Lemmy](./lemmy) | `dessalines/lemmy:0.19.5` | `8536` | — | Decentralised link aggregation; Reddit-like topic browsing. |
| [Mastodon](./mastodon) | `ghcr.io/mastodon/mastodon:latest` | `20151` | — | Server for Twitter-like microblogging; federated social network. |
| [Misskey](./misskey) | `misskey/misskey:latest` | `20158` | — | Microblogging platform forActivityPub; Japanese-originated. |
| [Noco Db](./noco-db) | `nocodb/nocodb:latest` | `20168` | — | Open-source Airtable alternative; turn databases into smart tables. |
| [Paperless-ngx](./paperless-ngx) | `linuxserver/paperless-ngx:latest` | `20189` | — | Document management system; scan, index, archive. |
| [Peertube](./peertube) | `chocobozzz/peertube:production-bookworm` | `20198` | ✅ | Decentralised video hosting platform; ActivityPub federated videos. |
| [Pixelfed](./pixelfed) | `zknt/pixelfed:latest` | `20206` | — | Federated photo sharing; Instagram alternative. |
| [Pleroma](./pleroma) | `elixir:1.16-alpine` | `20210` | — | Lightweight federated social network; alternative to Mastodon. |
| [Plume](./plume) | `plumeorg/plume:latest` | `7878` | — | Federation-friendly blogging platform; ActivityPub enabled. |
| [Rowshub](./rowshub) | `nocodb/nocodb:latest` | `20253` | — | Collaborative spreadsheet platform; Airtable alternative. |
| [Writefreely](./writefreely) | `writeas/writefreely:latest` | `20371` | — | Federated publishing platform; write and share articles. |

### Automation (15)

| Service | Image | Port | GPU | Description |
|---|---|---|:--:|---|
| [Ansible](./ansible) | `alpine/ansible:latest` | `20001` | — | Open source automation engine; IT automation and configuration management. |
| [Chef](./chef) | `chef/chef:latest` | `20405` | — | Automation platform for the most demanding environments. |
| [Consul](./consul) | `hashicorp/consul:latest` | `8500` | — | Service mesh solution; service discovery and configuration. |
| [Docker](./docker) | `docker:dind` | `20045` | — | Platform for creating and running containers; application virtualization. |
| [Hashicorp Tools](./hashicorp-tools) | `hashicorp/terraform:latest` | `20108` | — | Suite of infrastructure tools: Terraform, Vault, Consul, Nomad. |
| [Kubernetes](./kubernetes) | `registry.k8s.io/kube-apiserver:v1.31.0` | `20135` | ✅ | System for automating deployment, scaling, and management. |
| [Nomad](./nomad) | `hashicorp/nomad:latest` | `4646` | — | Workload orchestrator; schedule and run containers and VMs. |
| [Openshift](./openshift) | `quay.io/openshift/origin-cli:latest` | `20181` | — | Kubernetes platform; enterprise container application platform. |
| [Podman](./podman) | `quay.io/podman/stable:latest` | `20213` | — | Daemonless container engine; drop-in replacement for Docker. |
| [Pulumi](./pulumi) | `pulumi/pulumi:latest` | `20223` | — | Modern infrastructure as code; use real programming languages. |
| [Puppet](./puppet) | `puppet/puppetserver:latest` | `20224` | — | Configuration management tool; declarative infrastructure automation. |
| [Rancher](./rancher) | `rancher/rancher:latest` | `20233` | ✅ | Container management platform; multi-cluster Kubernetes management. |
| [Saltstack](./saltstack) | `saltstack/salt:latest` | `20262` | — | Event-driven automation engine; configuration management and orchestration. |
| [Terraform](./terraform) | `hashicorp/terraform:latest` | `20322` | ✅ | Infrastructure as code tool; provision and manage cloud resources. |
| [Vault](./vault) | `hashicorp/vault:latest` | `20346` | — | Secrets management platform; secure storage for sensitive data. |

### Audio (14)

| Service | Image | Port | GPU | Description |
|---|---|---|:--:|---|
| [Bazarr](./bazarr) | `lscr.io/linuxserver/bazarr:latest` | `6767` | — | Subtitle manager for Sonarr and Radarr; automatic download and management. |
| [Bifrost](./bifrost) | `alpine:3.20` | `20012` | — | Media server with Jellyfin-like features; open source and self-hosted. |
| [Emby](./emby) | `linuxserver/emby:latest` | `8096` | ✅ | Media system for organizing and streaming video, music, and photos. |
| [Flameborn](./flameborn) | `alpine:3.20` | `20070` | — | Open source media server; modern interface with advanced features. |
| [Jackett](./jackett) | `lscr.io/linuxserver/jackett:latest` | `9117` | — | API for torrent indexers; acts as a bridge between downloaders and indexers. |
| [Jellyfin](./jellyfin) | `jellyfin/jellyfin:latest` | `20117` | ✅ | Free and open source media system; fork of Emby with complete privacy focus. |
| [Lidarr](./lidarr) | `lscr.io/linuxserver/lidarr:latest` | `8686` | — | PVR for music; automatically downloads and organizes music albums. |
| [Medusa](./medusa) | `lscr.io/linuxserver/medusa:latest` | `8081` | — | Alternative to Sonarr; PVR for TV shows with extensive customization. |
| [Plex](./plex) | `linuxserver/plex:latest` | `32400` | ✅ | Media server for organizing and streaming your media library. |
| [Prowlarr](./prowlarr) | `lscr.io/linuxserver/prowlarr:latest` | `9696` | — | Indexing manager for Sonarr, Radarr, Lidarr, and Readarr; manages indexers. |
| [Radarr](./radarr) | `lscr.io/linuxserver/radarr:latest` | `20230` | — | PVR for movie fans; manages and automatically downloads films. |
| [Readarr](./readarr) | `lscr.io/linuxserver/readarr:develop` | `20235` | — | Book/PDF/EPUB/MOBI/AZW3 article librarian; manages book torrents and Usenet. |
| [Sonarr](./sonarr) | `lscr.io/linuxserver/sonarr:latest` | `8989` | — | PVR for TV shows; manages and automatically downloads series episodes. |
| [Streama](./streama) | `eclipse-temurin:17-jre` | `20304` | ✅ | Self-hosted Netflix clone; organize and stream your media collection. |

### Content Management Systems (14)

| Service | Image | Port | GPU | Description |
|---|---|---|:--:|---|
| [Craftcms](./craftcms) | `craftcms/nginx:8.2` | `20037` | — | Flexible content management; developer-friendly CMS. |
| [Directus](./directus) | `directus/directus:latest` | `8055` | — | Open-source Data Platform; turn any SQL database into a CMS. |
| [Drupal](./drupal) | `drupal:latest` | `20054` | — | Open-source CMS; flexible and extensible content management. |
| [Expressionengine](./expressionengine) | `php:8.2-apache` | `20066` | — | Flexible CMS; simple yet powerful content management. |
| [Ghost](./ghost) | `ghost:5-alpine` | `2368` | — | Publishing platform; focused on publishing and journalism. |
| [Joomla](./joomla) | `joomla:latest` | `20120` | — | Open-source CMS; easy to use with extensions. |
| [Kentico](./kentico) | `mcr.microsoft.com/dotnet/aspnet:8.0` | `20124` | — | All-in-one CMS; e-commerce and online marketing platform. |
| [Keystone](./keystone) | `node:20-alpine` | `20127` | — | Node.js GraphQL CMS; flexible and extensible. |
| [Payloadcms](./payloadcms) | `node:20-alpine` | `20194` | — | React-powered Node.js CMS; modern and customizable. |
| [Sitecore](./sitecore) | `mcr.microsoft.com/dotnet/aspnet:8.0` | `20283` | — | Enterprise CMS; .NET-based content management system. |
| [Strapi](./strapi) | `naskio/strapi:latest` | `20303` | — | Headless CMS; customizable and API-first. |
| [Typo3](./typo3) | `ghcr.io/typo3/core-testing-php82:latest` | `20341` | — | Open-source CMS; enterprise-grade content management. |
| [Umbraco](./umbraco) | `mcr.microsoft.com/dotnet/aspnet:8.0` | `20343` | — | Open-source CMS; built on .NET and ASP.NET. |
| [Wordpress](./wordpress) | `wordpress:latest` | `20369` | — | Web publishing platform; blogging and CMS with massive plugin ecosystem. |

### Backup (12)

| Service | Image | Port | GPU | Description |
|---|---|---|:--:|---|
| [Amanda](./amanda) | `ubuntu:24.04` | `20402` | — | Advanced Maryland Automatic Network Disk Archiver. |
| [Backuppc](./backuppc) | `adferrand/backuppc:latest` | `20007` | — | High-performance clientless backup system; server and desktop backup. |
| [Bacula](./bacula) | `ubuntu:24.04` | `20008` | — | Enterprise backup solution; network backup management. |
| [Borgbackup](./borgbackup) | `ghcr.io/borgmatic-collective/borgmatic:latest` | `20017` | — | Deduplicating backup program; efficient storage for backups. |
| [Duplicati](./duplicati) | `linuxserver/duplicati:latest` | `8200` | — | Backup tool; encrypt, compress and schedule backups. |
| [Owncloud](./owncloud) | `owncloud/server:latest` | `20188` | — | Open source alternative for file sharing; server and clients. |
| [Restic](./restic) | `restic/restic:latest` | `20243` | — | Fast backup program; easy to use with encryption and compression. |
| [Rsnapshot](./rsnapshot) | `linuxserver/rsnapshot:latest` | `20255` | — | Filesystem snapshot utility; rsync-based backup tool. |
| [Rsync](./rsync) | `eeacms/rsync:latest` | `20257` | — | Fast and versatile file copying tool; delta sync and backup. |
| [Sia](./sia) | `ghcr.io/siafoundation/renterd:latest` | `20280` | — | Decentralized cloud storage; cryptocurrency-based storage. |
| [Storj](./storj) | `storjlabs/storagenode:latest` | `14002` | — | Decentralized cloud storage; peer-to-peer storage network. |
| [Urbackup](./urbackup) | `uroni/urbackup-server:latest` | `55414` | — | Client/server backup solution; efficient backup and recovery. |

### Database Management (12)

| Service | Image | Port | GPU | Description |
|---|---|---|:--:|---|
| [Cassandra](./cassandra) | `cassandra:5` | `9042` | — | Highly scalable NoSQL database; column-family store designed for large datasets. |
| [Clickhouse](./clickhouse) | `clickhouse/clickhouse-server:latest` | `8123` | ✅ | Column-oriented database management system for OLAP and analytical workloads. |
| [Couchdb](./couchdb) | `couchdb:3` | `5984` | — | ouchdb-style JSON document database with MVCC and multi-master replication |
| [Duckdb](./duckdb) | `davidgasquez/duckdb:latest` | `20055` | — | In-process SQL OLAP database similar to SQLite but for analytics. |
| [Influxdb](./influxdb) | `influxdb:2` | `8086` | — | Time-series database optimized for metrics, events, and real-time analytics. |
| [Mariadb Columnstore](./mariadb-columnstore) | `mariadb/columnstore:latest` | `20150` | — | Columnar storage engine for MariaDB; optimized for analytics workloads. |
| [Mongodb](./mongodb) | `mongo:7` | `27017` | — | Document-oriented NoSQL database; stores JSON-like documents with flexible schemas. |
| [MySQL / MariaDB](./mysql-mariadb) | `mariadb:11` | `20161` | — | Popular relational database; MariaDB is a drop-in MySQL compatible alternative. |
| [Neo4J](./neo4j) | `neo4j:5` | `7474` | — | Graph database optimized for storing and querying relationships between data. |
| [Postgresql](./postgresql) | `postgres:16-alpine` | `20217` | — | Powerful open-source relational database; extensible, ACID-compliant with JSONB support. |
| [Redis](./redis) | `redis:7-alpine` | `20239` | — | In-memory key-value store; used as database, cache, and message broker. |
| [Sqlite](./sqlite) | `keinos/sqlite3:latest` | `20295` | — | Lightweight, file-based relational database; embedded database for most applications. |

### Security (12)

| Service | Image | Port | GPU | Description |
|---|---|---|:--:|---|
| [Certbot](./certbot) | `certbot/certbot:latest` | `20026` | — | Let's Encrypt client; automatic certificate management. |
| [Cfssl](./cfssl) | `cfssl/cfssl:latest` | `8888` | — | CloudFlare's PKI toolkit; certificate authority and tools. |
| [Elk](./elk) | `sebp/elk:latest` | `5601` | — | Elasticsearch, Logstash, Kibana; log analysis stack. |
| [Graylog](./graylog) | `graylog/graylog:6.1` | `20106` | — | Open source log management platform; centralized log management. |
| [Hashicorp Vault](./hashicorp-vault) | `hashicorp/vault:latest` | `20109` | — | Secrets management and encryption; secure key storage. |
| [Ossec](./ossec) | `atomicorp/ossec-docker:latest` | `1514` | — | Host-based intrusion detection system; log analysis and monitoring. |
| [Snort](./snort) | `ciscotalos/snort3:latest` | `20287` | — | Network intrusion detection and prevention system. |
| [Splunk](./splunk) | `splunk/splunk:latest` | `20292` | — | Enterprise SIEM platform; log analysis and monitoring |
| [Step Certificates](./step-certificates) | `smallstep/step-ca:latest` | `20301` | — | Private CA; X.509 PKI and ACME server. |
| [Suricata](./suricata) | `jasonish/suricata:latest` | `20315` | — | Network threat detection engine; IDS/IPS/NSM. |
| [Wazuh](./wazuh) | `wazuh/wazuh-manager:4.9.2` | `55000` | — | Open source security platform; XDR and SIEM capabilities. |
| [Zeek](./zeek) | `zeek/zeek:latest` | `20382` | — | Network security monitoring; powerful traffic analysis. |

### Api Management (11)

| Service | Image | Port | GPU | Description |
|---|---|---|:--:|---|
| [Ambassador](./ambassador) | `docker.io/emissaryingress/emissary:3.9.1` | `20403` | — | L7 load balancer; Kubernetes-native application delivery controller. |
| [Apache Apisix](./apache-apisix) | `apache/apisix:latest` | `9080` | — | Real-time API gateway; built on etcd and Lua. |
| [Caddy](./caddy) | `caddy:alpine` | `20022` | — | Easy to run HTTP web server; automatic HTTPS and simple configuration. |
| [Envoy](./envoy) | `envoyproxy/envoy:v1.31-latest` | `10000` | — | High-performance proxy; service mesh and edge proxy solution. |
| [Haproxy](./haproxy) | `haproxy:lts-alpine` | `20107` | — | Reliable, high-performance TCP/HTTP load balancer. |
| [Kong](./kong) | `kong/kong:latest` | `20133` | — | Kong Gateway; cloud-native API, LLM, and MCP gateway solution. |
| [Koryo](./koryo) | `alpine:3.20` | `20134` | — | Simple API gateway; lightweight and fast reverse proxy. |
| [Microk8S](./microk8s) | `ubuntu:24.04` | `20154` | — | Lightweight Kubernetes distribution; edge and IoT deployment. |
| [Nginx](./nginx) | `nginx:alpine` | `20166` | — | Web server and reverse proxy; high-performance HTTP server. |
| [Traefik](./traefik) | `traefik:v3.2` | `20332` | — | Modern reverse proxy; automatic service discovery and routing. |
| [Tyk](./tyk) | `tykio/tyk-gateway:latest` | `20340` | — | Open source API gateway; full lifecycle API management. |

### Database Tools (11)

| Service | Image | Port | GPU | Description |
|---|---|---|:--:|---|
| [Adminer](./adminer) | `adminer:latest` | `20395` | — | Tool for managing MySQL, PostgreSQL, SQLite, and other databases. |
| [Citus](./citus) | `citusdata/citus:12` | `20029` | — | Extension to PostgreSQL; real-time analytics and scaling. |
| [CockroachDB](./cockroachdb) | `cockroachdb/cockroach:latest` | `20035` | — | Cloud-native relational database; distributed SQL database. |
| [Dbeaver](./dbeaver) | `dbeaver/cloudbeaver:latest` | `8978` | — | Universal database tool; supports all major databases. |
| [Foundationdb](./foundationdb) | `foundationdb/foundationdb:7.3.27` | `4500` | — | Ordered key-value database; transactions and scalability. |
| [Pgadmin](./pgadmin) | `dpage/pgadmin4:latest` | `20199` | — | Web-based PostgreSQL database management tool; GUI for PostgreSQL. |
| [Phpmyadmin](./phpmyadmin) | `phpmyadmin:latest` | `20203` | — | Web interface for MySQL database management. |
| [Planetscale](./planetscale) | `vitess/lite:latest` | `15000` | — | Serverless MySQL platform; branchable databases. |
| [Prisma](./prisma) | `node:20-alpine` | `5555` | — | Database toolkit; type-safe ORM with migrations. |
| [Supabase](./supabase) | `supabase/postgres:15.8.1.020` | `20310` | — | Firebase alternative; open-source backend for web apps. |
| [Timescaledb](./timescaledb) | `timescale/timescaledb:latest-pg16` | `20329` | — | PostgreSQL extension for time-series data; SQL for time-series. |

### File (11)

| Service | Image | Port | GPU | Description |
|---|---|---|:--:|---|
| [Cloudflare R2](./cloudflare-r2) | `minio/minio:latest` | `9000` | — | S3-compatible object storage alternative to S3 with no egress fees |
| [Filebrowser](./filebrowser) | `filebrowser/filebrowser:latest` | `20069` | — | Web-based file manager with authentication; manages files and folders via browser. |
| [Ipfs](./ipfs) | `ipfs/kubo:latest` | `5001` | — | Protocol for decentralized file sharing; distributed content addressing. |
| [Minio](./minio) | `quay.io/minio/minio:latest` | `20157` | — | High-performance object storage; S3-compatible. |
| [Nextcloud](./nextcloud) | `nextcloud:stable` | `20165` | — | Suite of client-server software for file syncing, collaboration, and video conferencing. |
| [Pydio Cells](./pydio-cells) | `linuxserver/pydio-cells:latest` | `20226` | — | Enterprise file sharing and sync platform; modern alternative to Nextcloud. |
| [Rclone](./rclone) | `rclone/rclone:latest` | `5572` | — | Command-line program for syncing files and directories to cloud storage. |
| [Rclone Browser](./rclone-browser) | `rclone/rclone:latest` | `20234` | — | GUI for Rclone; manage cloud storage with local file browser interface. |
| [Seafile](./seafile) | `seafileltd/seafile-mc:latest` | `20266` | — | Professional file sync and share solution; focuses on efficiency and privacy. |
| [Syncthing](./syncthing) | `linuxserver/syncthing:latest` | `8384` | — | Continuous file synchronization; peer-to-peer sync without central server. |
| [Tahoe Lafs](./tahoe-lafs) | `tahoelafs/base:latest` | `3456` | — | Decentralized, fault-tolerant, encrypted file storage grid. |

### Ai (9)

| Service | Image | Port | GPU | Description |
|---|---|---|:--:|---|
| [Gpt Engineer](./gpt-engineer) | `python:3.11-slim` | `20102` | ✅ | AI-powered code generation tool; create projects from descriptions. |
| [Gpt4All](./gpt4all) | `python:3.11-slim` | `20103` | ✅ | Software and models for running LLMs on consumer devices. |
| [Jan](./jan) | `python:3.11-slim` | `1337` | ✅ | Desktop app for running open-source models locally with GPU acceleration. |
| [Koboldai](./koboldai) | `koboldai/koboldai:latest` | `20130` | ✅ | UI for running language models; originally for GPT novels. |
| [Localai](./localai) | `localai/localai:latest` | `20143` | ✅ | Open-source AI engine for local LLMs, vision, voice, image, and video models. |
| [Ollama](./ollama) | `ollama/ollama:latest` | `11434` | ✅ | Get started with Llama, Gemma, and other language models locally. |
| [Private Gpt](./private-gpt) | `3x3cut0r/privategpt:latest` | `20220` | — | Open-source API layer turning local models into production AI apps. |
| [Text Generation Webui](./text-generation-webui) | `atinoda/text-generation-webui:default` | `7860` | — | User interface for running LLMs locally; extensive model support. |
| [Vllm](./vllm) | `vllm/vllm-openai:latest` | `20351` | ✅ | Fast library for LLM inference and serving; high-throughput inference engine. |

### Development (9)

| Service | Image | Port | GPU | Description |
|---|---|---|:--:|---|
| [Drone](./drone) | `drone/drone:2` | `20052` | — | Continuous integration system; container-based CI/CD. |
| [Forgejo](./forgejo) | `codeberg.org/forgejo/forgejo:9` | `20073` | — | Fork of Gitea; community-driven Git service. |
| [Gitea](./gitea) | `gitea/gitea:latest` | `20090` | — | Lightweight Git service; alternative to GitHub/GitLab. |
| [Gitlab](./gitlab) | `gitlab/gitlab-ce:latest` | `20093` | — | Git platform with CI/CD; open-source DevOps platform. |
| [Gitlab Ci](./gitlab-ci) | `gitlab/gitlab-runner:latest` | `8093` | — | Built-in CI/CD for GitLab; automated testing and deployment. |
| [Gogs](./gogs) | `gogs/gogs:latest` | `20098` | — | Simple Git service; lightweight and easy to install. |
| [Jenkins](./jenkins) | `jenkins/jenkins:lts` | `20119` | — | Open source automation server; CI/CD for builds and tests. |
| [Sourcehut](./sourcehut) | `alpine:3.20` | `20290` | — | Hosting service for open source projects; git hosting and CI. |
| [Woodpecker Ci](./woodpecker-ci) | `woodpeckerci/woodpecker-server:latest` | `20368` | — | Lightweight CI/CD system; fork of Drone. |

### News (9)

| Service | Image | Port | GPU | Description |
|---|---|---|:--:|---|
| [Instapaper](./instapaper) | `alpine:3.20` | `20116` | — | Web article saver; read later and save content |
| [Linkace](./linkace) | `linkace/linkace:simple` | `20141` | — | Link shortener and bookmark manager; save and share URLs. |
| [Pinboard](./pinboard) | `alpine:3.20` | `20205` | — | Social bookmarking service; save and share links |
| [Pocket](./pocket) | `alpine:3.20` | `20212` | — | Save articles for later reading; privacy-focused alternative |
| [Raindrop Io](./raindrop-io) | `alpine:3.20` | `20231` | — | Bookmarking service; save and organize bookmarks |
| [Semantic Scholar](./semantic-scholar) | `python:3.11-slim` | `20269` | — | AI-powered research tool; academic paper search |
| [Shaarli](./shaarli) | `ghcr.io/shaarli/shaarli:latest` | `20276` | — | Minimalist bookmarking service; personal and lightweight. |
| [Wallabag](./wallabag) | `wallabag/wallabag:latest` | `20354` | — | Read it later; web article scraper and read-later application. |
| [Zza](./zza) | `alpine:3.20` | `20392` | — | Self-hosted link reader; read and save links for later. |

### Authentication (8)

| Service | Image | Port | GPU | Description |
|---|---|---|:--:|---|
| [Authelia](./authelia) | `authelia/authelia:latest` | `9091` | — | Identity and Access Proxy providing 2FA, SSO, and access controls for services. |
| [Keycloak](./keycloak) | `quay.io/keycloak/keycloak:latest` | `20125` | — | Open-source Identity and Access Management; OAuth2, OIDC, SAML provider. |
| [Lychee](./lychee) | `lycheeorg/lychee:latest` | `20145` | — | Photo management web application; organizes and displays photos with user auth. |
| [Oidc Proxy](./oidc-proxy) | `quay.io/oauth2-proxy/oauth2-proxy:latest` | `4180` | — | Single sign-on solution for legacy applications using OAuth2/OIDC. |
| [Passbolt](./passbolt) | `passbolt/passbolt:latest` | `20193` | — | Open Source password manager for teams; designed for business use. |
| [Privacyidea](./privacyidea) | `python:3.11-slim` | `20219` | — | Multi-factor authentication server supporting TOTP, HOTP, and WebAuthn. |
| [Societies](./societies) | `alpine:3.20` | `20289` | — | Social login provider; bridges social accounts with local accounts. |
| [Vaultwarden](./vaultwarden) | `vaultwarden/server:latest` | `20347` | — | Unofficial Bitwarden server implementation; lightweight and fast. |

### Chat (8)

| Service | Image | Port | GPU | Description |
|---|---|---|:--:|---|
| [Briar](./briar) | `alpine:3.20` | `20018` | — | Peer-to-peer messaging app; works over Tor and Bluetooth. |
| [Discord](./discord) | `alpine:3.20` | `20044` | — | Self-hosted Discord alternative; open source communication platform |
| [Matrix Synapse](./matrix-synapse) | `matrixdotorg/synapse:latest` | `8008` | — | Decentralized communication protocol server; bridges to other services. |
| [Mattermost](./mattermost) | `mattermost/mattermost-team-edition:latest` | `8065` | — | Open source Slack alternative; self-hosted team chat platform. |
| [Rocket Chat](./rocket-chat) | `registry.rocket.chat/rocketchat/rocket.chat:latest` | `20250` | — | Web chat platform for teams; built with Meteor.js framework. |
| [Sessions](./sessions) | `alpine:3.20` | `20274` | — | Encrypted messaging app; decentralized and privacy-focused. |
| [Zeronet](./zeronet) | `nofish/zeronet:latest` | `20384` | — | Decentralized websites using Bitcoin crypto and BitTorrent swarm. |
| [Zulip](./zulip) | `zulip/docker-zulip:latest` | `20391` | — | Groups chat app that’s designed to feel like email, with conversation threads. |

### Monitoring (8)

| Service | Image | Port | GPU | Description |
|---|---|---|:--:|---|
| [Alertmanager](./alertmanager) | `prom/alertmanager:latest` | `9093` | — | Alert handler for Prometheus; route and silencing alerts. |
| [Cloud Foundry](./cloud-foundry) | `alpine:3.20` | `20031` | — | Cloud-native platform; PaaS for app deployment. |
| [Jaeger](./jaeger) | `jaegertracing/all-in-one:latest` | `16686` | — | Distributed tracing; monitoring microservices performance. |
| [Mesos](./mesos) | `alpine:3.20` | `5050` | — | Distributed systems kernel; orchestrate containers and apps. |
| [Mimir](./mimir) | `grafana/mimir:latest` | `20155` | — | Grafana's long-term storage for Prometheus; scalable metrics. |
| [Thanos](./thanos) | `quay.io/thanos/thanos:v0.37.2` | `10902` | — | Highly available Prometheus; long-term storage solution. |
| [Victoriametrics](./victoriametrics) | `victoriametrics/victoria-metrics:latest` | `8428` | — | Ultra-high performing time series database; Prometheus compatible. |
| [Zipkin](./zipkin) | `openzipkin/zipkin:latest` | `9411` | — | Distributed tracing system; gather timing information. |

### Music (8)

| Service | Image | Port | GPU | Description |
|---|---|---|:--:|---|
| [Airsonic Advanced](./airsonic-advanced) | `lscr.io/linuxserver/airsonic-advanced:latest` | `20399` | — | Music server with multi-user support; stream your music anywhere. |
| [Ampache](./ampache) | `ampache/ampache:latest` | `20404` | ✅ | Web-based audio file manager; provides streaming and management interface. |
| [Funkwhale](./funkwhale) | `funkwhale/all-in-one:latest` | `20084` | ✅ | Peer-to-peer music sharing; listen and share music in a friendly way. |
| [Koel](./koel) | `phanan/koel:latest` | `20132` | ✅ | Simple web-based audio file management; personal cloud for music. |
| [Mopidy](./mopidy) | `wernight/mopidy:latest` | `6680` | ✅ | Extendable music server; Python-based with plugin architecture. |
| [Navidrome](./navidrome) | `deluan/navidrome:latest` | `4533` | — | Modern and lightweight Go/NodeJS music server; compatible with Subsonic API. |
| [Subsonic](./subsonic) | `lscr.io/linuxserver/airsonic-advanced:latest` | `4040` | — | Web media streaming platform; the progenitor for many forks. |
| [Swifty](./swifty) | `alpine:3.20` | `20316` | — | Simple and fast music server; lightweight alternative to Airsonic. |

### Rss (8)

| Service | Image | Port | GPU | Description |
|---|---|---|:--:|---|
| [Feedbin](./feedbin) | `alpine:3.20` | `20067` | — | Web-based feed reader; social features and excellent filtering capabilities. |
| [Freshrss](./freshrss) | `lscr.io/linuxserver/freshrss:latest` | `20079` | — | Free and open-source web RSS reader; multi-user self-hosted feed reader. |
| [Miniflux](./miniflux) | `miniflux/miniflux:latest` | `20156` | — | Simple and fast RSS reader; minimalist UI with excellent readability. |
| [Newsblur](./newsblur) | `python:3.11-slim` | `20163` | — | News reader with smart filtering; self-hosted version for news aggregation. |
| [Reader Rise](./reader-rise) | `alpine:3.20` | `20236` | — | Self-hosted Feedbin alternative; clean UI with OPML import/export. |
| [Rsshub](./rsshub) | `diygod/rsshub:latest` | `1200` | — | Everything is an RSS feed; aggregates content from various sources to RSS. |
| [The Old Reader](./the-old-reader) | `alpine:3.20` | `20324` | — | Social RSS reader; sharing and discovery of RSS feeds. |
| [Tiny Tiny Rss](./tiny-tiny-rss) | `php:8.2-fpm` | `20331` | — | Web-based news reader; customizable and extensible RSS aggregator. |

### Vpn (7)

| Service | Image | Port | GPU | Description |
|---|---|---|:--:|---|
| [Algo Vpn](./algo-vpn) | `ubuntu:24.04` | `20401` | — | VPN servers; deploy IPsec VPN on popular cloud providers. |
| [Openconnect](./openconnect) | `ubuntu:24.04` | `20177` | — | SSL VPN solution; Cisco AnyConnect compatible. |
| [Openvpn](./openvpn) | `kylemanna/openvpn:latest` | `1194` | — | SSL VPN solution; secure networking and remote access. |
| [Outline Vpn](./outline-vpn) | `quay.io/outline/shadowbox:stable` | `20187` | — | Secure team network access; Shadowsocks-based proxy. |
| [Tailscale](./tailscale) | `tailscale/tailscale:latest` | `41641` | — | WireGuard-based mesh VPN; zero-config networking. |
| [Wireguard](./wireguard) | `lscr.io/linuxserver/wireguard:latest` | `51820` | — | Next-generation VPN protocol; fast and modern VPN solution. |
| [Zerotier](./zerotier) | `zerotier/zerotier:latest` | `9993` | — | Smart networking platform; SD-WAN and SDN capabilities. |

### Additional Services (6)

| Service | Image | Port | GPU | Description |
|---|---|---|:--:|---|
| [Cloudflare Argo](./cloudflare-argo) | `cloudflare/cloudflared:latest` | `2000` | — | Cloudflare's smart routing; secure and fast connections. |
| [Cloudflared](./cloudflared) | `cloudflare/cloudflared:latest` | `20032` | — | Cloudflare Tunnel; connect services without public IP. |
| [Health Checker](./health-checker) | `lscr.io/linuxserver/healthchecks:latest` | `20110` | — | Simple monitoring tool; check service availability. |
| [Nginx Proxy Manager](./nginx-proxy-manager) | `jc21/nginx-proxy-manager:latest` | `20167` | — | Web interface for managing Nginx proxies; simple reverse proxy. |
| [Openresty](./openresty) | `openresty/openresty:alpine` | `20179` | — | NGINX with Lua; high-performance web platform. |
| [Uptime Kuma](./uptime-kuma) | `louislam/uptime-kuma:1` | `20344` | — | Self-hosting status page; monitor websites and services. |

### File Sharing (6)

| Service | Image | Port | GPU | Description |
|---|---|---|:--:|---|
| [Afs](./afs) | `alpine:3.20` | `7000` | — | Andrew File System; distributed file system. |
| [Ftp Server](./ftp-server) | `delfer/alpine-ftp-server:latest` | `20082` | — | File Transfer Protocol server; traditional file access. |
| [Nfs](./nfs) | `itsthenetwork/nfs-server-alpine:latest` | `2049` | — | Network File System; share file systems on Unix/Linux. |
| [Samba](./samba) | `dperson/samba:latest` | `20265` | — | SMB/CIFS file sharing; access from Windows and Linux. |
| [Sftp Server](./sftp-server) | `atmoz/sftp:latest` | `20275` | — | SSH File Transfer Protocol; secure file transfer. |
| [Webdav](./webdav) | `bytemark/webdav:latest` | `20359` | — | HTTP-based file management protocol; file sharing over HTTP. |

### Password Management (6)

| Service | Image | Port | GPU | Description |
|---|---|---|:--:|---|
| [Bitwarden](./bitwarden) | `vaultwarden/server:latest` | `20013` | — | Open source password manager; secure storage for passwords and notes. |
| [Bitwarden RS (Vaultwarden)](./bitwarden-rs) | `vaultwarden/server:latest` | `20014` | — | Lightweight Bitwarden server; Rust implementation of Bitwarden API. |
| [Keepassxc](./keepassxc) | `lscr.io/linuxserver/keepassxc:latest` | `20123` | — | Password manager; store your passwords safely and access everywhere. |
| [Keypass](./keypass) | `alpine:3.20` | `20126` | — | Simple password generator; create secure random passwords. |
| [Lesspass](./lesspass) | `node:20-alpine` | `20138` | — | Generate passwords from master password; deterministic password generator. |
| [Pass](./pass) | `alpine:3.20` | `20192` | — | Simple password management; command-line password store. |

### Media Conversion (5)

| Service | Image | Port | GPU | Description |
|---|---|---|:--:|---|
| [Ffmpeg](./ffmpeg) | `linuxserver/ffmpeg:latest` | `20068` | ✅ | Command-line video/audio processing; convert and edit media files. |
| [Handbrake](./handbrake) | `linuxserver/handbrake:latest` | `5800` | ✅ | Video transcoder; convert videos to optimized formats. |
| [Makemkv](./makemkv) | `jlesage/makemkv:latest` | `20149` | ✅ | DVD/Blu-ray copying tool; extract video from optical discs. |
| [Sub Converter](./sub-converter) | `python:3.11-slim` | `25500` | — | Subtitle file converter; convert between different subtitle formats. |
| [Tautulli](./tautulli) | `lscr.io/linuxserver/tautulli:latest` | `8181` | ✅ | Plex media server monitoring; track usage and analytics. |

### Payments (5)

| Service | Image | Port | GPU | Description |
|---|---|---|:--:|---|
| [Hyperswitch](./hyperswitch) | `juspaydotin/hyperswitch-router:latest` | `20113` | — | Open-source payments infrastructure; routing, retries, and reconciliation. |
| [Kill Bill](./kill-bill) | `killbill/killbill:latest` | `20128` | — | Open source payment system; subscriptions and billing platform. |
| [Omnipay](./omnipay) | `php:8.2-fpm` | `20172` | — | Multi-gateway payment processing library for PHP. |
| [Payment Js](./payment-js) | `node:20-alpine` | `20195` | — | Simple payment processing; handle credit cards and payments. |
| [Payum](./payum) | `php:8.2-fpm` | `20197` | — | PHP Payment Management Library; comprehensive payment processing. |

### Video (5)

| Service | Image | Port | GPU | Description |
|---|---|---|:--:|---|
| [Kodi](./kodi) | `lscr.io/linuxserver/webtop:ubuntu-kde` | `20131` | ✅ | Free and open source media center; entertainment system hub. |
| [Recast](./recast) | `alpine:3.20` | `20237` | — | Media server with transcoding; organize and watch your TV shows/movies. |
| [Streamlink](./streamlink) | `python:3.11-slim` | `20305` | — | Command-line utility to extract streams from various services. |
| [Stremth](./stremth) | `alpine:3.20` | `20306` | — | Stream management and organization tool; acts as a media hub. |
| [Vlc Frontend](./vlc-frontend) | `lscr.io/linuxserver/webtop:ubuntu-kde` | `20350` | — | Web interface for managing and watching VLC content. |

### Virtualization (4)

| Service | Image | Port | GPU | Description |
|---|---|---|:--:|---|
| [Kvm](./kvm) | `qemux/qemu:latest` | `20136` | ✅ | Full virtualization for Linux; kernel-based virtual machine. |
| [Libvirt](./libvirt) | `ubuntu:24.04` | `16509` | ✅ | Open source virtualization API; manage VMs and containers. |
| [Qemu](./qemu) | `qemux/qemu:latest` | `20228` | ✅ | Open source emulator and virtualization; hardware emulation. |
| [Truenas](./truenas) | `ubuntu:24.04` | `20335` | ✅ | Storage platform; FreeNAS successor for NAS and file sharing. |

### Search Engines (Specialized) (3)

| Service | Image | Port | GPU | Description |
|---|---|---|:--:|---|
| [Bleve](./bleve) | `golang:1.23-alpine` | `20015` | — | Modern text search and analytics; Go full-text search library. |
| [Vespa](./vespa) | `vespaengine/vespa:latest` | `20349` | — | Feature-rich search and ML engine; big data serving platform. |
| [Zomboyin](./zomboyin) | `alpine:3.20` | `20389` | — | Full-text search engine; JavaScript-based search. |

### Network (2)

| Service | Image | Port | GPU | Description |
|---|---|---|:--:|---|
| [Opennebula](./opennebula) | `opennebula/opennebula:latest` | `9869` | ✅ | Open source cloud management platform; IaaS solution. |
| [Openstack](./openstack) | `ubuntu:24.04` | `20183` | ✅ | Cloud operating system; build public and private clouds. |

## Full index (A–Z)

| Service | Category | Port |
|---|---|---|
| [42Links](./42links) | Self Hosting Solutions | `8080` |
| [92Five](./92five) | Self Hosting Solutions | `20393` |
| [Ackee](./ackee) | Analytics | `20394` |
| [Adminer](./adminer) | Database Tools | `20395` |
| [Adyen Proxy](./adyen-proxy) | Self Hosting Solutions | `20396` |
| [Afs](./afs) | File Sharing | `7000` |
| [Afterlogic](./afterlogic) | Email | `20397` |
| [Agent Vault](./agent-vault) | Self Hosting Solutions | `20398` |
| [Airsonic Advanced](./airsonic-advanced) | Music | `20399` |
| [Akkoma](./akkoma) | Self Hosting Solutions | `20400` |
| [Alertmanager](./alertmanager) | Monitoring | `9093` |
| [Alfresco](./alfresco) | Self Hosting Solutions | `20408` |
| [Algo Vpn](./algo-vpn) | Vpn | `20401` |
| [Aliasvault](./aliasvault) | Self Hosting Solutions | `20409` |
| [Amanda](./amanda) | Backup | `20402` |
| [Ambassador](./ambassador) | Api Management | `20403` |
| [Ampache](./ampache) | Music | `20404` |
| [Ansible](./ansible) | Automation | `20001` |
| [Answer](./answer) | Self Hosting Solutions | `20411` |
| [Anythingllm](./anythingllm) | Self Hosting Solutions | `20412` |
| [Apache Apisix](./apache-apisix) | Api Management | `9080` |
| [Appflowy](./appflowy) | Productivity | `20002` |
| [Appwrite](./appwrite) | Self Hosting Solutions | `20003` |
| [Archivebox](./archivebox) | Self Hosting Solutions | `20413` |
| [Authelia](./authelia) | Authentication | `9091` |
| [Awstats](./awstats) | Analytics | `20004` |
| [Axigen](./axigen) | Email | `20005` |
| [B1Gmail](./b1gMail) | Self Hosting Solutions | `20006` |
| [Backuppc](./backuppc) | Backup | `20007` |
| [Bacula](./bacula) | Backup | `20008` |
| [Baikal](./baikal) | Self Hosting Solutions | `20009` |
| [Bamboo](./bamboo) | Self Hosting Solutions | `8085` |
| [Bar Assistant](./bar-assistant) | Self Hosting Solutions | `20010` |
| [Baserow](./baserow) | Email | `20011` |
| [Bazarr](./bazarr) | Audio | `6767` |
| [Bifrost](./bifrost) | Audio | `20012` |
| [Bitwarden](./bitwarden) | Password Management | `20013` |
| [Bitwarden RS (Vaultwarden)](./bitwarden-rs) | Password Management | `20014` |
| [Bleve](./bleve) | Search Engines (Specialized) | `20015` |
| [Booklore](./booklore) | Self Hosting Solutions | `6060` |
| [Bookstack](./bookstack) | Productivity | `20016` |
| [Bookwyrm](./bookwyrm) | Social | `8000` |
| [Borgbackup](./borgbackup) | Backup | `20017` |
| [Briar](./briar) | Chat | `20018` |
| [Browserstack Turboscale](./browserstack-turboscale) | Self Hosting Solutions | `20019` |
| [Buddy Enterprise](./buddy-enterprise) | Self Hosting Solutions | `20020` |
| [Bumpress](./bumpress) | Self Hosting Solutions | `20419` |
| [C15T](./c15t) | Self Hosting Solutions | `20021` |
| [Caddy](./caddy) | Api Management | `20022` |
| [Calibre](./calibre) | Self Hosting Solutions | `8083` |
| [Canvas Lms](./canvas-lms) | Self Hosting Solutions | `3000` |
| [Cap](./cap) | Self Hosting Solutions | `20023` |
| [Cassandra](./cassandra) | Database Management | `9042` |
| [Castopod](./castopod) | Self Hosting Solutions | `20024` |
| [Centrifugo](./centrifugo) | Self Hosting Solutions | `20025` |
| [Cerbos](./cerbos) | Self Hosting Solutions | `3592` |
| [Certbot](./certbot) | Security | `20026` |
| [Cfssl](./cfssl) | Security | `8888` |
| [Cgit](./cgit) | Self Hosting Solutions | `20027` |
| [Changedetection](./changedetection) | Self Hosting Solutions | `20422` |
| [Chef](./chef) | Automation | `20405` |
| [Chronograf](./chronograf) | Analytics | `20028` |
| [Citus](./citus) | Database Tools | `20029` |
| [Claude Code](./claude-code) | Self Hosting Solutions | `20530` |
| [Clickhouse](./clickhouse) | Database Management | `8123` |
| [Client Management](./client-management) | Crm | `20030` |
| [Cloud Foundry](./cloud-foundry) | Monitoring | `20031` |
| [Cloudflare Argo](./cloudflare-argo) | Additional Services | `2000` |
| [Cloudflare R2](./cloudflare-r2) | File | `9000` |
| [Cloudflared](./cloudflared) | Additional Services | `20032` |
| [Cloudron](./cloudron) | Self Hosting Solutions | `20033` |
| [Cluster Control](./cluster-control) | Self Hosting Solutions | `20034` |
| [Cockpit](./cockpit) | Self Hosting Solutions | `9090` |
| [CockroachDB](./cockroachdb) | Database Tools | `20035` |
| [Collabora Online](./collabora-online) | Self Hosting Solutions | `9980` |
| [Comfyui](./comfyui) | Self Hosting Solutions | `8188` |
| [Commentario](./commentario) | Self Hosting Solutions | `20036` |
| [Conduit](./conduit) | Self Hosting Solutions | `6167` |
| [Consul](./consul) | Automation | `8500` |
| [Couchdb](./couchdb) | Database Management | `5984` |
| [Craftcms](./craftcms) | Content Management Systems | `20037` |
| [Crucial](./crucial) | Self Hosting Solutions | `20038` |
| [Crush Propulsion](./crush-propulsion) | Social | `20039` |
| [Daisy](./daisy) | Self Hosting Solutions | `20040` |
| [Datasette](./datasette) | Self Hosting Solutions | `8001` |
| [Davical](./davical) | Self Hosting Solutions | `20041` |
| [Davis](./davis) | Self Hosting Solutions | `20042` |
| [Dbeaver](./dbeaver) | Database Tools | `8978` |
| [Debops](./debops) | Self Hosting Solutions | `20434` |
| [Depay](./depay) | Self Hosting Solutions | `20043` |
| [Dify](./dify) | Self Hosting Solutions | `20531` |
| [Directus](./directus) | Content Management Systems | `8055` |
| [Discord](./discord) | Chat | `20044` |
| [Discourse](./discourse) | Self Hosting Solutions | `20436` |
| [Docker](./docker) | Automation | `20045` |
| [Docuddle](./docuddle) | Self Hosting Solutions | `20046` |
| [Documenso](./documenso) | Self Hosting Solutions | `20047` |
| [Dolibarr](./dolibarr) | Crm | `20048` |
| [Dovecot](./dovecot) | Email | `20049` |
| [Dpaste](./dpaste) | Self Hosting Solutions | `20050` |
| [Dreamfactory](./dreamfactory) | Self Hosting Solutions | `20051` |
| [Drone](./drone) | Development | `20052` |
| [Druid](./druid) | Self Hosting Solutions | `20053` |
| [Drupal](./drupal) | Content Management Systems | `20054` |
| [Duckdb](./duckdb) | Database Management | `20055` |
| [Duckduckgo Proxy](./duckduckgo-proxy) | Self Hosting Solutions | `5000` |
| [Duplicati](./duplicati) | Backup | `8200` |
| [Easypanel](./easypanel) | Self Hosting Solutions | `20056` |
| [Ejabberd](./ejabberd) | Self Hosting Solutions | `5280` |
| [Ekso](./ekso) | Self Hosting Solutions | `20057` |
| [Elasticsearch](./elasticsearch) | Search Engines | `9200` |
| [Element](./element) | Self Hosting Solutions | `20438` |
| [Element Web](./element-web) | Self Hosting Solutions | `20058` |
| [Element Web App](./element-web-app) | Self Hosting Solutions | `20059` |
| [Elixire](./elixire) | Self Hosting Solutions | `20060` |
| [Elk](./elk) | Security | `5601` |
| [Emby](./emby) | Audio | `8096` |
| [Emqx](./emqx) | Self Hosting Solutions | `18083` |
| [Enclosed](./enclosed) | Self Hosting Solutions | `8787` |
| [Engity Bifrost](./engity-bifrost) | Self Hosting Solutions | `20061` |
| [Envoy](./envoy) | Api Management | `10000` |
| [Epicyon](./epicyon) | Self Hosting Solutions | `20062` |
| [Ergo](./ergo) | Self Hosting Solutions | `20441` |
| [Erpnext](./erpnext) | Crm | `20063` |
| [Excalidraw](./excalidraw) | Self Hosting Solutions | `20064` |
| [Exim](./exim) | Email | `20065` |
| [Expressionengine](./expressionengine) | Content Management Systems | `20066` |
| [Feedbin](./feedbin) | Rss | `20067` |
| [Ffmpeg](./ffmpeg) | Media Conversion | `20068` |
| [Filebrowser](./filebrowser) | File | `20069` |
| [Flameborn](./flameborn) | Audio | `20070` |
| [Fmd Server](./fmd-server) | Self Hosting Solutions | `20071` |
| [Focalboard](./focalboard) | Productivity | `20072` |
| [Forgejo](./forgejo) | Development | `20073` |
| [Formio](./formio) | Self Hosting Solutions | `3001` |
| [Forward Email](./forward-email) | Self Hosting Solutions | `20074` |
| [Fossbilling](./fossbilling) | Crm | `20075` |
| [Foundationdb](./foundationdb) | Database Tools | `4500` |
| [Framadate](./framadate) | Self Hosting Solutions | `20076` |
| [Fredy](./fredy) | Self Hosting Solutions | `9998` |
| [Freepbx](./freepbx) | Self Hosting Solutions | `20077` |
| [Freeswitch](./freeswitch) | Self Hosting Solutions | `20078` |
| [Freshrss](./freshrss) | Rss | `20079` |
| [Friendica](./friendica) | Social | `20080` |
| [Frigate](./frigate) | Self Hosting Solutions | `20081` |
| [Ftp Server](./ftp-server) | File Sharing | `20082` |
| [Full Help](./full-help) | Self Hosting Solutions | `20083` |
| [Funkwhale](./funkwhale) | Music | `20084` |
| [Fusio](./fusio) | Self Hosting Solutions | `20085` |
| [Gamevault](./gamevault) | Self Hosting Solutions | `20086` |
| [Garagehq](./garagehq) | Self Hosting Solutions | `3900` |
| [Gaseous Server](./gaseous-server) | Self Hosting Solutions | `5198` |
| [Gathio](./gathio) | Self Hosting Solutions | `20087` |
| [Geo2Tz](./geo2tz) | Self Hosting Solutions | `20088` |
| [Ghost](./ghost) | Content Management Systems | `2368` |
| [Ghostery](./ghostery) | Self Hosting Solutions | `20089` |
| [Gitea](./gitea) | Development | `20090` |
| [Github Ntfy](./github-ntfy) | Self Hosting Solutions | `20091` |
| [Github Runner](./github-runner) | Self Hosting Solutions | `20092` |
| [Gitlab](./gitlab) | Development | `20093` |
| [Gitlab Ci](./gitlab-ci) | Development | `8093` |
| [Glance](./glance) | Self Hosting Solutions | `20094` |
| [Glitchtip](./glitchtip) | Self Hosting Solutions | `20095` |
| [Globaleaks](./globaleaks) | Self Hosting Solutions | `20096` |
| [Gnuseed](./gnuseed) | Social | `20097` |
| [Go Feature Flag](./go-feature-flag) | Self Hosting Solutions | `1031` |
| [Goaccess](./goaccess) | Analytics | `7890` |
| [Gogs](./gogs) | Development | `20098` |
| [Gomodel](./gomodel) | Self Hosting Solutions | `20099` |
| [Google Cse Proxy](./google-cse-proxy) | Self Hosting Solutions | `20100` |
| [Gordian](./gordian) | Self Hosting Solutions | `20101` |
| [Gotify](./gotify) | Self Hosting Solutions | `20448` |
| [Gpt Engineer](./gpt-engineer) | Ai | `20102` |
| [Gpt4All](./gpt4all) | Ai | `20103` |
| [Grafana](./grafana) | Analytics | `20104` |
| [Graphite](./graphite) | Analytics | `20105` |
| [Graylog](./graylog) | Security | `20106` |
| [Habitica](./habitica) | Self Hosting Solutions | `20451` |
| [Halo](./halo) | Self Hosting Solutions | `20452` |
| [Handbrake](./handbrake) | Media Conversion | `5800` |
| [Haproxy](./haproxy) | Api Management | `20107` |
| [Hashicorp Tools](./hashicorp-tools) | Automation | `20108` |
| [Hashicorp Vault](./hashicorp-vault) | Security | `20109` |
| [Health Checker](./health-checker) | Additional Services | `20110` |
| [Hedgedoc](./hedgedoc) | Productivity | `20111` |
| [Homeassistant](./homeassistant) | Self Hosting Solutions | `20455` |
| [Homer](./homer) | Self Hosting Solutions | `20112` |
| [Hoppscotch](./hoppscotch) | Self Hosting Solutions | `20456` |
| [Hyperswitch](./hyperswitch) | Payments | `20113` |
| [Iredmail](./iRedMail) | Email | `20114` |
| [Icehound](./icehound) | Analytics | `20115` |
| [Immich](./immich) | Self Hosting Solutions | `2283` |
| [Influxdb](./influxdb) | Database Management | `8086` |
| [Instapaper](./instapaper) | News | `20116` |
| [Ipfs](./ipfs) | File | `5001` |
| [Jackett](./jackett) | Audio | `9117` |
| [Jaeger](./jaeger) | Monitoring | `16686` |
| [Jan](./jan) | Ai | `1337` |
| [Jellyfin](./jellyfin) | Audio | `20117` |
| [Jellyfin Library](./jellyfin-library) | Self Hosting Solutions | `20118` |
| [Jenkins](./jenkins) | Development | `20119` |
| [Joomla](./joomla) | Content Management Systems | `20120` |
| [Joplin](./joplin) | Productivity | `22300` |
| [Kanboard](./kanboard) | Self Hosting Solutions | `20121` |
| [Kapacitor](./kapacitor) | Analytics | `9092` |
| [Kbin](./kbin) | Social | `20122` |
| [Keepassxc](./keepassxc) | Password Management | `20123` |
| [Kentico](./kentico) | Content Management Systems | `20124` |
| [Keycloak](./keycloak) | Authentication | `20125` |
| [Keypass](./keypass) | Password Management | `20126` |
| [Keystone](./keystone) | Content Management Systems | `20127` |
| [Kill Bill](./kill-bill) | Payments | `20128` |
| [Kiwix](./kiwix) | Search Engines | `20129` |
| [Koboldai](./koboldai) | Ai | `20130` |
| [Kodi](./kodi) | Video | `20131` |
| [Koel](./koel) | Music | `20132` |
| [Kong](./kong) | Api Management | `20133` |
| [Koryo](./koryo) | Api Management | `20134` |
| [Kubernetes](./kubernetes) | Automation | `20135` |
| [Kvm](./kvm) | Virtualization | `20136` |
| [Langflow](./langflow) | Self Hosting Solutions | `20463` |
| [Laverna](./laverna) | Productivity | `20137` |
| [Lemmy](./lemmy) | Social | `8536` |
| [Lesspass](./lesspass) | Password Management | `20138` |
| [Libervrt](./libervrt) | Self Hosting Solutions | `20139` |
| [Library Genesis](./library-genesis) | Search Engines | `20140` |
| [Librechat](./librechat) | Self Hosting Solutions | `20465` |
| [Libvirt](./libvirt) | Virtualization | `16509` |
| [Lidarr](./lidarr) | Audio | `8686` |
| [Linkace](./linkace) | News | `20141` |
| [Litellm](./litellm) | Self Hosting Solutions | `4000` |
| [Lms](./lms) | Self Hosting Solutions | `20142` |
| [Lobechat](./lobechat) | Self Hosting Solutions | `20469` |
| [Localai](./localai) | Ai | `20143` |
| [Logstash](./logstash) | Analytics | `9600` |
| [Loki](./loki) | Analytics | `3100` |
| [Lxd](./lxd) | Self Hosting Solutions | `20144` |
| [Lychee](./lychee) | Authentication | `20145` |
| [Magento](./magento) | Crm | `20146` |
| [Mailcow](./mailcow) | Email | `20147` |
| [Mailu](./mailu) | Email | `20148` |
| [Makemkv](./makemkv) | Media Conversion | `20149` |
| [Mariadb Columnstore](./mariadb-columnstore) | Database Management | `20150` |
| [Mastodon](./mastodon) | Social | `20151` |
| [Matomo](./matomo) | Analytics | `20152` |
| [Matrix Synapse](./matrix-synapse) | Chat | `8008` |
| [Mattermost](./mattermost) | Chat | `8065` |
| [Medusa](./medusa) | Audio | `8081` |
| [Meilisearch](./meilisearch) | Search Engines | `7700` |
| [Mesos](./mesos) | Monitoring | `5050` |
| [Metabase](./metabase) | Self Hosting Solutions | `20553` |
| [Metager](./metager) | Search Engines | `20153` |
| [Metube](./metube) | Self Hosting Solutions | `20475` |
| [Microk8S](./microk8s) | Api Management | `20154` |
| [Mimir](./mimir) | Monitoring | `20155` |
| [Mindsdb](./mindsdb) | Self Hosting Solutions | `20476` |
| [Miniflux](./miniflux) | Rss | `20156` |
| [Minio](./minio) | File | `20157` |
| [Misskey](./misskey) | Social | `20158` |
| [Modoboa](./modoboa) | Email | `20159` |
| [Mollie Proxy](./mollie-proxy) | Self Hosting Solutions | `20160` |
| [Mongodb](./mongodb) | Database Management | `27017` |
| [Mopidy](./mopidy) | Music | `6680` |
| [Mylar3](./mylar3) | Self Hosting Solutions | `20539` |
| [MySQL / MariaDB](./mysql-mariadb) | Database Management | `20161` |
| [Navidrome](./navidrome) | Music | `4533` |
| [Neo4J](./neo4j) | Database Management | `7474` |
| [Netlify](./netlify) | Self Hosting Solutions | `20162` |
| [Newsblur](./newsblur) | Rss | `20163` |
| [Nextchat](./nextchat) | Self Hosting Solutions | `20164` |
| [Nextcloud](./nextcloud) | File | `20165` |
| [Nfs](./nfs) | File Sharing | `2049` |
| [Nginx](./nginx) | Api Management | `20166` |
| [Nginx Proxy Manager](./nginx-proxy-manager) | Additional Services | `20167` |
| [Noco Db](./noco-db) | Social | `20168` |
| [Nomad](./nomad) | Automation | `4646` |
| [Notejot](./notejot) | Productivity | `20169` |
| [Notion Clone](./notion-clone) | Self Hosting Solutions | `20170` |
| [October Cms](./october-cms) | Crm | `20171` |
| [Odoo](./odoo) | Crm | `8069` |
| [Oidc Proxy](./oidc-proxy) | Authentication | `4180` |
| [Ollama](./ollama) | Ai | `11434` |
| [Omnipay](./omnipay) | Payments | `20172` |
| [Online Invoicing](./online-invoicing) | Self Hosting Solutions | `20173` |
| [Opencart](./opencart) | Crm | `20174` |
| [Openclaw](./openclaw) | Self Hosting Solutions | `20175` |
| [Opencode](./opencode) | Self Hosting Solutions | `20176` |
| [Openconnect](./openconnect) | Vpn | `20177` |
| [Opennebula](./opennebula) | Network | `9869` |
| [Openproject](./openproject) | Productivity | `20178` |
| [Openresty](./openresty) | Additional Services | `20179` |
| [OpenSearch](./opensearch) | Search Engines | `20180` |
| [Openshift](./openshift) | Automation | `20181` |
| [Opensmtpd](./opensmtpd) | Email | `20182` |
| [Openstack](./openstack) | Network | `20183` |
| [Openvpn](./openvpn) | Vpn | `1194` |
| [Openwebui](./openwebui) | Analytics | `20184` |
| [Organizr](./organizr) | Self Hosting Solutions | `20185` |
| [Ossec](./ossec) | Security | `1514` |
| [Outline](./outline) | Productivity | `20186` |
| [Outline Vpn](./outline-vpn) | Vpn | `20187` |
| [Owncloud](./owncloud) | Backup | `20188` |
| [Paperless-ngx](./paperless-ngx) | Social | `20189` |
| [Para](./para) | Self Hosting Solutions | `20190` |
| [Partkeep System](./partkeep-system) | Crm | `20191` |
| [Pass](./pass) | Password Management | `20192` |
| [Passbolt](./passbolt) | Authentication | `20193` |
| [Payloadcms](./payloadcms) | Content Management Systems | `20194` |
| [Payment Js](./payment-js) | Payments | `20195` |
| [Paypal Proxy](./paypal-proxy) | Self Hosting Solutions | `20196` |
| [Payum](./payum) | Payments | `20197` |
| [Peertube](./peertube) | Social | `20198` |
| [Pgadmin](./pgadmin) | Database Tools | `20199` |
| [Pgdog](./pgdog) | Self Hosting Solutions | `20200` |
| [Phice](./phice) | Self Hosting Solutions | `20201` |
| [Phorge](./phorge) | Self Hosting Solutions | `20202` |
| [Phpmyadmin](./phpmyadmin) | Database Tools | `20203` |
| [Piefed](./piefed) | Self Hosting Solutions | `20204` |
| [Pinboard](./pinboard) | News | `20205` |
| [Pinecone](./pinecone) | Search Engines | `6333` |
| [Pixelfed](./pixelfed) | Social | `20206` |
| [Plane](./plane) | Productivity | `20207` |
| [Planetscale](./planetscale) | Database Tools | `15000` |
| [Plausible](./plausible) | Self Hosting Solutions | `20208` |
| [Plausible Analytics](./plausible-analytics) | Analytics | `20209` |
| [Pleroma](./pleroma) | Social | `20210` |
| [Plex](./plex) | Audio | `32400` |
| [Plume](./plume) | Social | `7878` |
| [Plunker](./plunker) | Self Hosting Solutions | `20211` |
| [Pocket](./pocket) | News | `20212` |
| [Pocket Id](./pocket-id) | Self Hosting Solutions | `1411` |
| [Pocketbase](./pocketbase) | Self Hosting Solutions | `8090` |
| [Podman](./podman) | Automation | `20213` |
| [Portainer](./portainer) | Self Hosting Solutions | `9443` |
| [Postal](./postal) | Self Hosting Solutions | `20214` |
| [Poste Io](./poste-io) | Self Hosting Solutions | `20215` |
| [Postfix](./postfix) | Email | `20216` |
| [Postgresql](./postgresql) | Database Management | `20217` |
| [Prestashop](./prestashop) | Crm | `20218` |
| [Prisma](./prisma) | Database Tools | `5555` |
| [Privacyidea](./privacyidea) | Authentication | `20219` |
| [Private Gpt](./private-gpt) | Ai | `20220` |
| [Prometheus](./prometheus) | Analytics | `20221` |
| [Prowlarr](./prowlarr) | Audio | `9696` |
| [Proxmox](./proxmox) | Self Hosting Solutions | `20222` |
| [Pulumi](./pulumi) | Automation | `20223` |
| [Puppet](./puppet) | Automation | `20224` |
| [Pushbits](./pushbits) | Self Hosting Solutions | `20225` |
| [Pydio Cells](./pydio-cells) | File | `20226` |
| [Qdrant](./qdrant) | Search Engines | `20227` |
| [Qemu](./qemu) | Virtualization | `20228` |
| [R2](./r2) | Self Hosting Solutions | `20229` |
| [Radarr](./radarr) | Audio | `20230` |
| [Radicale](./radicale) | Self Hosting Solutions | `5232` |
| [Raindrop Io](./raindrop-io) | News | `20231` |
| [Rainloop](./rainloop) | Email | `20232` |
| [Rancher](./rancher) | Automation | `20233` |
| [Rclone](./rclone) | File | `5572` |
| [Rclone Browser](./rclone-browser) | File | `20234` |
| [Readarr](./readarr) | Audio | `20235` |
| [Reader Rise](./reader-rise) | Rss | `20236` |
| [Recast](./recast) | Video | `20237` |
| [Redirect](./redirect) | Self Hosting Solutions | `20238` |
| [Redis](./redis) | Database Management | `20239` |
| [Repo Flow](./repo-flow) | Self Hosting Solutions | `20240` |
| [Reservo](./reservo) | Self Hosting Solutions | `20241` |
| [Resourcespace](./resourcespace) | Self Hosting Solutions | `20242` |
| [Restic](./restic) | Backup | `20243` |
| [Restreamer](./restreamer) | Self Hosting Solutions | `20244` |
| [Restyaboard](./restyaboard) | Productivity | `20245` |
| [Revent](./revent) | Self Hosting Solutions | `20246` |
| [Revert](./revert) | Self Hosting Solutions | `20247` |
| [Rgit](./rgit) | Self Hosting Solutions | `20248` |
| [Rhode Code](./rhode-code) | Self Hosting Solutions | `20249` |
| [Rocket Chat](./rocket-chat) | Chat | `20250` |
| [Roundcube](./roundcube) | Email | `20251` |
| [Routr](./routr) | Self Hosting Solutions | `20252` |
| [Rowshub](./rowshub) | Social | `20253` |
| [Rs Short](./rs-short) | Self Hosting Solutions | `20254` |
| [Rsnapshot](./rsnapshot) | Backup | `20255` |
| [Rss Bridge](./rss-bridge) | Self Hosting Solutions | `20256` |
| [Rsshub](./rsshub) | Rss | `1200` |
| [Rsync](./rsync) | Backup | `20257` |
| [Rudderstack](./rudderstack) | Self Hosting Solutions | `20258` |
| [Rukovoditel](./rukovoditel) | Self Hosting Solutions | `20259` |
| [Sabre Dav](./sabre-dav) | Self Hosting Solutions | `20260` |
| [Saleor](./saleor) | Crm | `20261` |
| [Saltstack](./saltstack) | Automation | `20262` |
| [Salut A Toi](./salut-a-toi) | Self Hosting Solutions | `20263` |
| [Sama](./sama) | Self Hosting Solutions | `20264` |
| [Samba](./samba) | File Sharing | `20265` |
| [Seafile](./seafile) | File | `20266` |
| [SearXNG](./searxng) | Search Engines | `20267` |
| [Seaweedfs](./seaweedfs) | Self Hosting Solutions | `9333` |
| [Sefaria](./sefaria) | Search Engines | `20268` |
| [Semantic Scholar](./semantic-scholar) | News | `20269` |
| [Sendmail](./sendmail) | Email | `20270` |
| [Sendy](./sendy) | Self Hosting Solutions | `20271` |
| [Sentry](./sentry) | Analytics | `20272` |
| [Seppo](./seppo) | Self Hosting Solutions | `20273` |
| [Sessions](./sessions) | Chat | `20274` |
| [Sftp Server](./sftp-server) | File Sharing | `20275` |
| [Shaarli](./shaarli) | News | `20276` |
| [Shkeeper](./shkeeper) | Self Hosting Solutions | `20277` |
| [Shopis](./shopis) | Crm | `20278` |
| [Shopware](./shopware) | Crm | `20279` |
| [Sia](./sia) | Backup | `20280` |
| [Signoz](./signoz) | Self Hosting Solutions | `20281` |
| [Sip3](./sip3) | Self Hosting Solutions | `20282` |
| [Sitecore](./sitecore) | Content Management Systems | `20283` |
| [Smederee](./smederee) | Self Hosting Solutions | `20284` |
| [Smite](./smite) | Self Hosting Solutions | `20285` |
| [Snipe It](./snipe-it) | Crm | `20286` |
| [Snort](./snort) | Security | `20287` |
| [Snypy](./snypy) | Self Hosting Solutions | `20288` |
| [Societies](./societies) | Authentication | `20289` |
| [Socks5 Proxy Server](./socks5-proxy-server) | Self Hosting Solutions | `1080` |
| [Sogo](./sogo) | Email | `20000` |
| [Solr](./solr) | Search Engines | `8983` |
| [Sonarr](./sonarr) | Audio | `8989` |
| [Sourcehut](./sourcehut) | Development | `20290` |
| [Speed Test](./speed-test) | Self Hosting Solutions | `20291` |
| [Splunk](./splunk) | Security | `20292` |
| [Spoolman](./spoolman) | Self Hosting Solutions | `20293` |
| [Spree Commerce](./spree-commerce) | Crm | `20294` |
| [Sqlite](./sqlite) | Database Management | `20295` |
| [Squidex](./squidex) | Self Hosting Solutions | `20296` |
| [Squirrelmail](./squirrelmail) | Email | `20297` |
| [Srs](./srs) | Self Hosting Solutions | `1985` |
| [Stack Auth](./stack-auth) | Self Hosting Solutions | `20298` |
| [Stalwart Mail](./stalwart-mail) | Self Hosting Solutions | `20299` |
| [Standard Notes](./standard-notes) | Productivity | `20300` |
| [Step Certificates](./step-certificates) | Security | `20301` |
| [Stirling Pdf](./stirling-pdf) | Self Hosting Solutions | `20302` |
| [Storj](./storj) | Backup | `14002` |
| [Strapi](./strapi) | Content Management Systems | `20303` |
| [Streama](./streama) | Audio | `20304` |
| [Streamlink](./streamlink) | Video | `20305` |
| [Stremth](./stremth) | Video | `20306` |
| [Stripe Proxy](./stripe-proxy) | Self Hosting Solutions | `20307` |
| [Stripe Self Hosted](./stripe-self-hosted) | Self Hosting Solutions | `20308` |
| [Sub Converter](./sub-converter) | Media Conversion | `25500` |
| [Subsonic](./subsonic) | Music | `4040` |
| [Subtitle Converter](./subtitle-converter) | Self Hosting Solutions | `20309` |
| [Supabase](./supabase) | Database Tools | `20310` |
| [Supers3Cret](./supers3cret) | Self Hosting Solutions | `20311` |
| [Supportpal](./supportpal) | Self Hosting Solutions | `20312` |
| [Surfer](./surfer) | Self Hosting Solutions | `20313` |
| [Surge](./surge) | Self Hosting Solutions | `20314` |
| [Suricata](./suricata) | Security | `20315` |
| [Svix](./svix) | Self Hosting Solutions | `8071` |
| [Swifty](./swifty) | Music | `20316` |
| [Sylius](./sylius) | Crm | `20317` |
| [Synapse](./synapse) | Self Hosting Solutions | `20318` |
| [Syncthing](./syncthing) | File | `8384` |
| [Tahoe Lafs](./tahoe-lafs) | File | `3456` |
| [Taiga](./taiga) | Productivity | `20319` |
| [Tailscale](./tailscale) | Vpn | `41641` |
| [Taskcafe](./taskcafe) | Productivity | `3333` |
| [Tautulli](./tautulli) | Media Conversion | `8181` |
| [Teikei](./teikei) | Self Hosting Solutions | `20320` |
| [Telebugs](./telebugs) | Self Hosting Solutions | `20321` |
| [Tempo](./tempo) | Analytics | `3200` |
| [Terraform](./terraform) | Automation | `20322` |
| [Text Gen Inference](./text-gen-inference) | Self Hosting Solutions | `20323` |
| [Text Generation Webui](./text-generation-webui) | Ai | `7860` |
| [Thanos](./thanos) | Monitoring | `10902` |
| [The Old Reader](./the-old-reader) | Rss | `20324` |
| [Thelia](./thelia) | Self Hosting Solutions | `20325` |
| [Thumbor](./thumbor) | Self Hosting Solutions | `20326` |
| [Tigase](./tigase) | Self Hosting Solutions | `20327` |
| [Tileserver Gl](./tileserver-gl) | Self Hosting Solutions | `20328` |
| [Timescaledb](./timescaledb) | Database Tools | `20329` |
| [Tinode](./tinode) | Self Hosting Solutions | `20330` |
| [Tiny Tiny Rss](./tiny-tiny-rss) | Rss | `20331` |
| [Traefik](./traefik) | Api Management | `20332` |
| [Trailbase](./trailbase) | Self Hosting Solutions | `20333` |
| [Trigger Dev](./trigger-dev) | Self Hosting Solutions | `20334` |
| [Truenas](./truenas) | Virtualization | `20335` |
| [Tuleap](./tuleap) | Self Hosting Solutions | `20336` |
| [Turtl](./turtl) | Productivity | `20337` |
| [Tuwunel](./tuwunel) | Self Hosting Solutions | `20338` |
| [Txtdot](./txtdot) | Self Hosting Solutions | `20339` |
| [Tyk](./tyk) | Api Management | `20340` |
| [Typesense](./typesense) | Search Engines | `8108` |
| [Typo3](./typo3) | Content Management Systems | `20341` |
| [Umami](./umami) | Analytics | `20342` |
| [Umbraco](./umbraco) | Content Management Systems | `20343` |
| [Uptime Kuma](./uptime-kuma) | Additional Services | `20344` |
| [Urbackup](./urbackup) | Backup | `55414` |
| [Url To Png](./url-to-png) | Self Hosting Solutions | `20345` |
| [Vault](./vault) | Automation | `20346` |
| [Vaultwarden](./vaultwarden) | Authentication | `20347` |
| [Vercel](./vercel) | Self Hosting Solutions | `20348` |
| [Vespa](./vespa) | Search Engines (Specialized) | `20349` |
| [Victoriametrics](./victoriametrics) | Monitoring | `8428` |
| [Vlc Frontend](./vlc-frontend) | Video | `20350` |
| [Vllm](./vllm) | Ai | `20351` |
| [Wagmios](./wagmios) | Self Hosting Solutions | `20352` |
| [Wakapi](./wakapi) | Self Hosting Solutions | `20353` |
| [Wallabag](./wallabag) | News | `20354` |
| [Watchcode](./watchcode) | Self Hosting Solutions | `20355` |
| [Watchtower](./watchtower) | Self Hosting Solutions | `20356` |
| [Wazo](./wazo) | Self Hosting Solutions | `20357` |
| [Wazuh](./wazuh) | Security | `55000` |
| [Weaviate](./weaviate) | Search Engines | `20358` |
| [Webdav](./webdav) | File Sharing | `20359` |
| [Webiny](./webiny) | Self Hosting Solutions | `20360` |
| [Wekan](./wekan) | Productivity | `20361` |
| [Whoogle](./whoogle) | Search Engines | `20362` |
| [Wiki Js](./wiki-js) | Productivity | `20363` |
| [Wikipedia Kiwix](./wikipedia-kiwix) | Self Hosting Solutions | `20364` |
| [Wildduck](./wildduck) | Self Hosting Solutions | `20365` |
| [Wireguard](./wireguard) | Vpn | `51820` |
| [Wireguard Vpn](./wireguard-vpn) | Self Hosting Solutions | `20366` |
| [Woocommerce](./woocommerce) | Crm | `20367` |
| [Woodpecker Ci](./woodpecker-ci) | Development | `20368` |
| [Wordpress](./wordpress) | Content Management Systems | `20369` |
| [Workadventure](./workadventure) | Self Hosting Solutions | `20370` |
| [Writefreely](./writefreely) | Social | `20371` |
| [Xandikos](./xandikos) | Self Hosting Solutions | `20372` |
| [Xcpg](./xcpg) | Self Hosting Solutions | `20373` |
| [Yacy](./yacy) | Search Engines | `20374` |
| [Yarn Social](./yarn-social) | Self Hosting Solutions | `20375` |
| [Ydl Api Ng](./ydl-api-ng) | Self Hosting Solutions | `20376` |
| [Yeti Switch](./yeti-switch) | Self Hosting Solutions | `20377` |
| [Yetishare](./yetishare) | Self Hosting Solutions | `20378` |
| [Yourls](./yourls) | Self Hosting Solutions | `20379` |
| [Youtubedl Server](./youtubedl-server) | Self Hosting Solutions | `20380` |
| [Yt Dlp Web Ui](./yt-dlp-web-ui) | Self Hosting Solutions | `3033` |
| [Zed](./zed) | Self Hosting Solutions | `20381` |
| [Zeek](./zeek) | Security | `20382` |
| [Zeit](./zeit) | Self Hosting Solutions | `20383` |
| [Zeronet](./zeronet) | Chat | `20384` |
| [Zerotier](./zerotier) | Vpn | `9993` |
| [Zim](./zim) | Search Engines | `20385` |
| [Zimbra](./zimbra) | Email | `20386` |
| [Zimbra Collaboration](./zimbra-collaboration) | Self Hosting Solutions | `20387` |
| [Zincsearch](./zincsearch) | Self Hosting Solutions | `4080` |
| [Zipkin](./zipkin) | Monitoring | `9411` |
| [Zk Cloudserver](./zk-cloudserver) | Self Hosting Solutions | `20388` |
| [Zomboyin](./zomboyin) | Search Engines (Specialized) | `20389` |
| [Zot Oci Registry](./zot-oci-registry) | Self Hosting Solutions | `20390` |
| [Zulip](./zulip) | Chat | `20391` |
| [Zza](./zza) | News | `20392` |

