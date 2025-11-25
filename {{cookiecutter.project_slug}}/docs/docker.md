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

## Vulnerability Scanning

The project includes Trivy for scanning Docker images for vulnerabilities.

### Installation

Install Trivy:
```bash
# macOS
brew install trivy

# Linux
# See: https://aquasecurity.github.io/trivy/latest/getting-started/installation/
```

### Usage

**Scan after building:**
```bash
# Build and scan in one command
bash docker/build.sh --scan

# Or using Makefile
make docker-build-scan
```

**Scan an existing image:**
```bash
# Basic scan
bash docker/scan.sh

# Custom options
bash docker/scan.sh \
  --image my-image:tag \
  --severity CRITICAL,HIGH,MEDIUM \
  --format table

# Or using Makefile
make docker-scan
```

**Scan options:**
- `--image IMAGE`: Image to scan (default: project Docker image name)
- `--severity SEVERITIES`: Comma-separated list (CRITICAL, HIGH, MEDIUM, LOW, UNKNOWN)
- `--format FORMAT`: Output format (table, json, sarif)
- `--fail-on SEVERITY`: Exit with error if vulnerabilities of this severity are found

**CI/CD Integration:**
The scan script exits with code 1 if critical vulnerabilities are found, making it suitable for CI/CD pipelines:
```bash
bash docker/build.sh --scan || exit 1
```

