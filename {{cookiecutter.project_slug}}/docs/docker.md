# Docker Guide

## Images

- `docker/Dockerfile`: CUDA-enabled image using `nvidia/cuda:{{ cookiecutter.cuda_version }}-cudnn8-runtime-ubuntu{{ cookiecutter.base_ubuntu_version }}`. Requires NVIDIA Container Toolkit and x86_64 Linux host.
- `docker/Dockerfile.cpu`: CPU-only variant for Apple Silicon / non-NVIDIA hosts or CPU-only deployments.

## Build

### Using Make (Recommended)

```bash
# Build default image (auto-switches to CPU on ARM Macs)
make docker-build

# Build CPU image explicitly
make docker-build-cpu

# Build CUDA image (x86_64 Linux only)
make docker-build-cuda

# Build and scan in one command
make docker-build-scan
```

**Note:** On ARM Macs, the build script automatically switches to the CPU Dockerfile since CUDA images don't run natively on ARM.

### Using Scripts Directly

```bash
# Build default image
bash docker/build.sh

# Build CPU image
bash docker/build.sh --cpu

# Build with scan
bash docker/build.sh --scan
```

**Flags:**
- `--cpu`: Use CPU Dockerfile instead of CUDA
- `--scan`: Automatically run Trivy scan after building
- `--image IMAGE`: Specify custom image name
- `--target TARGET`: Specify build target (default: runtime)
- `--platform PLATFORM`: Override platform (e.g., `linux/amd64`)

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

The script automatically uses the CPU Dockerfile on ARM Macs since CUDA images don't run natively on ARM.

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
```

**Scan after building (using scripts):**
```bash
# Build and scan in one command
bash docker/build.sh --scan
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
make docker-build          # Build default image (auto-switches to CPU on ARM)
make docker-build-cpu      # Build CPU image explicitly
make docker-build-cuda    # Build CUDA image (x86_64 Linux only)
make docker-build-scan     # Build and scan default image
make docker-run           # Run the container
make docker-scan           # Scan existing image
```

## Platform Notes

- **x86_64 Linux**: Can build and run both CUDA and CPU images
- **ARM Macs**: Automatically uses CPU Dockerfile (CUDA images don't run natively)
- **CUDA images**: Require NVIDIA GPU and NVIDIA Container Toolkit

