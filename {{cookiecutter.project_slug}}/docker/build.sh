#!/usr/bin/env bash
set -euo pipefail

IMAGE="{{ cookiecutter.docker_image_name }}"
TARGET="runtime"
DOCKERFILE="docker/Dockerfile"
PLATFORM=""

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
    *)
      shift
      ;;
  esac
done

if [[ "$(uname -m)" == "arm64" && "$DOCKERFILE" != "docker/Dockerfile.cpu" ]]; then
  echo "⚠️  ARM host detected. Switching to CPU Dockerfile to avoid CUDA incompatibilities."
  DOCKERFILE="docker/Dockerfile.cpu"
fi

docker build ${PLATFORM} \
  -f "${DOCKERFILE}" \
  --target "${TARGET}" \
  -t "${IMAGE}" \
  .

