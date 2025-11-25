#!/usr/bin/env bash
set -euo pipefail

IMAGE="{{ cookiecutter.docker_image_name }}"
TARGET="runtime"
DOCKERFILE="docker/Dockerfile"
PLATFORM=""
SCAN_AFTER_BUILD=false
FORCE_CUDA=false

while [[ $# -gt 0 ]]; do
  case "$1" in
    --target)
      TARGET="$2"
      shift 2
      ;;
    --cpu)
      DOCKERFILE="docker/Dockerfile.cpu"
      shift
      ;;
    --platform)
      PLATFORM="--platform $2"
      shift 2
      ;;
    --image)
      IMAGE="$2"
      shift 2
      ;;
    --scan)
      SCAN_AFTER_BUILD=true
      shift
      ;;
    --force-cuda|--build-for-scan)
      FORCE_CUDA=true
      shift
      ;;
    *)
      shift
      ;;
  esac
done

if [[ "$(uname -m)" == "arm64" && "$DOCKERFILE" != "docker/Dockerfile.cpu" ]]; then
  if [[ "${FORCE_CUDA}" == "true" ]]; then
    echo "🔧 ARM host detected. Building CUDA image for linux/amd64 (for scanning only)."
    PLATFORM="--platform linux/amd64"
  else
    echo "⚠️  ARM host detected. Switching to CPU Dockerfile to avoid CUDA incompatibilities."
    echo "   Use --force-cuda or --build-for-scan to build CUDA image for scanning."
    DOCKERFILE="docker/Dockerfile.cpu"
  fi
fi

docker build ${PLATFORM} \
  -f "${DOCKERFILE}" \
  --target "${TARGET}" \
  -t "${IMAGE}" \
  .

if [[ "${SCAN_AFTER_BUILD}" == "true" ]]; then
  echo ""
  echo "🔍 Running Trivy vulnerability scan..."
  bash docker/scan.sh --image "${IMAGE}"
fi

