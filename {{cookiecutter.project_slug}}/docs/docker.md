# Docker Guide

## Images

- `docker/Dockerfile`: CUDA-first image using `nvidia/cuda:{{ cookiecutter.cuda_version }}-cudnn9-runtime-ubuntu{{ cookiecutter.base_ubuntu_version }}`. Requires NVIDIA Container Toolkit.
- `docker/Dockerfile.cpu`: CPU-safe variant for Apple Silicon / non-NVIDIA hosts.

## Build

```bash
bash docker/build.sh --target runtime
```

Flags:

- `--platform linux/amd64` for CUDA base images.
- `--platform linux/arm64` when building on Apple Silicon with the CPU Dockerfile.

## Run

```bash
bash docker/run.sh --gpus all --env-file .env
```

The script inspects host architecture and falls back to the CPU image on ARM by default. Override with `--force-cuda` if you are cross-building and have a compatible runtime.

## OS Packages

Base system libraries live in `docker/apt-packages.txt`. Edit this list to add drivers, ffmpeg, etc., keeping builds deterministic.

