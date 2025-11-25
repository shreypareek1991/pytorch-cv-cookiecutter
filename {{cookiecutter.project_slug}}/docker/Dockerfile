{% if cookiecutter.use_cuda_default == "y" -%}
ARG BASE_IMAGE=nvidia/cuda:{{ cookiecutter.cuda_version }}-cudnn8-runtime-ubuntu{{ cookiecutter.base_ubuntu_version }}
{% else -%}
ARG BASE_IMAGE=python:{{ cookiecutter.python_version }}-slim
{% endif %}
FROM ${BASE_IMAGE} AS base

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY docker/apt-packages.txt /tmp/apt-packages.txt

RUN apt-get update && \
    apt-get install -y --no-install-recommends software-properties-common && \
    add-apt-repository -y ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y --no-install-recommends python{{ cookiecutter.python_version }} python{{ cookiecutter.python_version }}-pip python{{ cookiecutter.python_version }}-venv && \
    update-alternatives --install /usr/bin/python3 python3 /usr/bin/python{{ cookiecutter.python_version }} 1 && \
    update-alternatives --install /usr/bin/pip3 pip3 /usr/bin/pip{{ cookiecutter.python_version }} 1 && \
    xargs -a /tmp/apt-packages.txt apt-get install -y --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /opt/app

COPY pyproject.toml uv.lock README.md ./
COPY requirements ./requirements
COPY src ./src
COPY scripts ./scripts
COPY configs ./configs

RUN python3 -m pip install --upgrade pip uv && \
    uv sync --frozen --python python{{ cookiecutter.python_version }} --extra deploy

FROM base AS runtime
CMD ["uv", "run", "python", "scripts/serve.py", "api"]

