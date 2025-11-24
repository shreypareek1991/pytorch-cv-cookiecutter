#!/usr/bin/env bash
set -euo pipefail

IMAGE="{{ cookiecutter.docker_image_name }}"
PORT=8000
GPU_FLAG=""
ARGS=()

while [[ $# -gt 0 ]]; do
  case "$1" in
    --gpus)
      GPU_FLAG="--gpus $2"
      shift 2
      ;;
    --port)
      PORT="$2"
      shift 2
      ;;
    --image)
      IMAGE="$2"
      shift 2
      ;;
    --force-cuda)
      GPU_FLAG="--gpus all"
      shift
      ;;
    *)
      ARGS+=("$1")
      shift
      ;;
  esac
done

if [[ "$(uname -m)" == "arm64" && -z "${GPU_FLAG}" ]]; then
  echo "ℹ️  Running in CPU mode on ARM host. Use --force-cuda if supported."
fi

docker run --rm -it \
  -p "${PORT}:8000" \
  ${GPU_FLAG:-} \
  -v "$(pwd)/artifacts:/opt/app/artifacts" \
  "${IMAGE}" \
  "${ARGS[@]}"

