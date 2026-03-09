# Docker — Overview

This document explains the project's Docker model and practical tips for building and running containers. It uses a simple metaphor: a Docker container is like a spaceship that must carry everything it needs to run on any host.

---

## Dockerfile (the blueprint)

The `Dockerfile` is read top-to-bottom; each instruction creates an image layer. Example base image used in this project:

```Dockerfile
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04
```

The base image provides an OS + GPU runtime. Use `runtime` images if you only need to run GPU workloads (not compile CUDA from source).

## Layers and caching

Each instruction (e.g., `RUN`, `COPY`) produces a layer. Docker caches layers — order your Dockerfile from least- to most-frequently changing to maximize cache reuse:

- Install OS packages (rarely changes)
- Install Python dependencies (changes occasionally)
- Copy application code (changes frequently)

Example pattern:

```Dockerfile
# Layer 1: system packages
RUN apt-get update && apt-get install -y python3.11 ffmpeg tzdata curl

# Layer 2: Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Layer 3: application code
COPY . .
```

`--no-cache-dir` keeps pip from storing wheels in the image and reduces final image size.

---

## What to install

Two categories of dependencies:

- System packages (via `apt-get`) — OS-level binaries like `ffmpeg`, `curl`.
- Language packages (via `pip`) — Python libraries listed in `requirements.txt`.

If a tool is a binary you would install on a fresh server, install it with `apt-get` in the image.

---

## Python version pitfalls

Ubuntu 22.04 ships with Python 3.10. If you install `python3-pip`, it installs pip for the system Python (3.10), not for a manually installed `python3.11`. To ensure `pip` targets Python 3.11, bootstrap pip into that interpreter:

```Dockerfile
RUN curl https://bootstrap.pypa.io/get-pip.py | python3.11
```

This ensures packages are installed into the correct Python runtime used by your app.

---

## Volumes (persisted data)

Containers are ephemeral by default. Use Docker volumes or bind mounts to persist data on the host.

Example `docker-compose.yml` volume mounts:

```yaml
services:
  app:
    volumes:
      - ./backend/stories.db:/app/stories.db
      - ./backend/config:/app/config
      - ./backend/logs:/app/logs
      - ./backend/app/video/media:/app/app/video/media
```

Format: `host_path:container_path`.

SQLite is a single file — without a mounted path, the database is lost when the container is replaced. Mount the SQLite file from the host to persist it.

Do not bake large media or generated files into images; mount them as volumes instead and add them to `.dockerignore`:

```
venv/
app/video/media
.env
```

---

## Environment variables and secrets

Never bake secrets into images. Use `env_file` or environment variables at runtime:

```yaml
services:
  app:
    env_file: .env
```

This injects secrets at container start without storing them in the image.

---

## GPU access

To give a container access to NVIDIA GPUs, the NVIDIA container toolkit must be configured and the compose spec should request device capabilities. Example (compose v2+):

```yaml
deploy:
  resources:
    reservations:
      devices:
        - driver: nvidia
          count: 1
          capabilities: [gpu]
```

Without GPU access, PyTorch falls back to CPU and workloads like TTS/Whisper slow significantly.

---

## Mental model (host ↔ container)

Host (Windows) contains persistent files and volumes. Container contains the runtime and application code. Volumes bridge the two so data persists and is shareable with the host.

Example components running in the container:

- Python 3.11 + pip
- PyTorch + CUDA
- TTS / Whisper
- FFmpeg
- FastAPI (exposed on port 8000)

---

## Common commands

```bash
# Build images
docker compose build

# Start in background
docker compose up -d

# View logs
docker compose logs -f

# Stop and remove containers (volumes remain)
docker compose down

# Rebuild then start
docker compose up --build -d
```

Key insight: images are immutable (built at build time); volumes and env files are the live data and secrets the container uses at runtime.

---

## Quick checklist

- Order Dockerfile instructions to maximize cache reuse.
- Install OS-level binaries with `apt-get` and language libs with `pip`.
- Bootstrap `pip` into non-system Python versions if needed.
- Use bind mounts/volumes for databases and media.
- Keep secrets out of images; use `env_file` or runtime env vars.
- Configure NVIDIA runtime and device reservations for GPU workloads.

---

If you'd like, I can also:

- add a short `docker-compose.example.yml` showing the minimal service config
- add a `.dockerignore` file tuned for this project

---

Last updated: cleaned and reformatted for GitHub-style Markdown.