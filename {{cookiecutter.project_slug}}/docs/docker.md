# Docker Guide

## Images

- `docker/Dockerfile`: CUDA-first image using `nvidia/cuda:{{ cookiecutter.cuda_version }}-cudnn9-runtime-ubuntu{{ cookiecutter.base_ubuntu_version }}`. Requires NVIDIA Container Toolkit.
- `docker/Dockerfile.cpu`: CPU-safe variant for Apple Silicon / non-NVIDIA hosts.

## Build

### Using Make (Recommended)

```bash
# Build default image (CUDA on x86, CPU on ARM)
make docker-build

# Build CPU image explicitly
make docker-build-cpu

# Build CUDA image (on ARM Mac: builds for linux/amd64, cannot run but can be scanned)
make docker-build-cuda

# Build and scan in one command
make docker-build-scan

# Build CUDA image and scan (useful on ARM Macs for vulnerability scanning)
make docker-build-cuda-scan
```

### Using Scripts Directly

```bash
bash docker/build.sh --target runtime
```

**Flags:**
- `--platform linux/amd64` for CUDA base images.
- `--platform linux/arm64` when building on Apple Silicon with the CPU Dockerfile.
- `--force-cuda` or `--build-for-scan`: Build CUDA image on ARM Macs for scanning (uses `--platform linux/amd64`). The image cannot run natively but can be scanned with Trivy. Requires Docker buildx (usually pre-installed with Docker Desktop).
- `--cpu`: Use CPU Dockerfile instead of CUDA.
- `--scan`: Automatically run Trivy scan after building.

## Run

### Using Make

```bash
# Run the container
make docker-run
```

### Using Scripts Directly

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

**Scan after building (using Make):**
```bash
# Build and scan default image
make docker-build-scan

# On ARM Mac: Build CUDA image for scanning (cannot run, but can be scanned)
make docker-build-cuda-scan
```

**Scan after building (using scripts):**
```bash
# Build and scan in one command
bash docker/build.sh --scan

# On ARM Mac: Build CUDA image for scanning
bash docker/build.sh --force-cuda --scan
```

**Scan an existing image (using Make):**
```bash
# Basic scan
make docker-scan
```

**Scan an existing image (using scripts):**
```bash
# Basic scan
bash docker/scan.sh

# Custom options
bash docker/scan.sh \
  --image my-image:tag \
  --severity CRITICAL,HIGH,MEDIUM \
  --format table
```

**Scan options:**
- `--image IMAGE`: Image to scan (default: project Docker image name)
- `--severity SEVERITIES`: Comma-separated list (CRITICAL, HIGH, MEDIUM, LOW, UNKNOWN)
- `--format FORMAT`: Output format (table, json, sarif)
- `--fail-on SEVERITY`: Exit with error if vulnerabilities of this severity are found

**CI/CD Integration:**
The scan script exits with code 1 if critical vulnerabilities are found, making it suitable for CI/CD pipelines:

```bash
# Using Make
make docker-build-scan || exit 1

# Using scripts
bash docker/build.sh --scan || exit 1
```

## Quick Reference: All Make Commands

```bash
# Docker operations
make docker-build          # Build default image
make docker-build-cpu      # Build CPU image
make docker-build-cuda     # Build CUDA image (cross-platform on ARM)
make docker-build-scan     # Build and scan default image
make docker-build-cuda-scan # Build CUDA image and scan (ARM Mac friendly)
make docker-run            # Run the container
make docker-scan           # Scan existing image
```

