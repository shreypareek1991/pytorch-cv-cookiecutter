# CUDA Dockerfile
# Base: NVIDIA CUDA runtime image (doesn't include Python)

FROM nvidia/cuda:{{ cookiecutter.cuda_version }}-cudnn8-runtime-ubuntu{{ cookiecutter.base_ubuntu_version }} AS base

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install Python (CUDA base doesn't include it)
RUN apt-get update && \
    apt-get install -y --no-install-recommends python3 python3-pip python3-venv && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /opt/app

# Install OS packages
COPY docker/apt-packages.txt /tmp/apt-packages.txt
RUN apt-get update && \
    xargs -a /tmp/apt-packages.txt apt-get install -y --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Copy project files
COPY pyproject.toml uv.lock README.md ./
COPY src ./src
COPY scripts ./scripts
COPY configs ./configs

# Install Python dependencies
RUN python3 -m pip install --upgrade pip uv && \
    uv sync --frozen --python python3 --extra deploy

FROM base AS runtime
CMD ["uv", "run", "python", "scripts/serve.py", "api"]
