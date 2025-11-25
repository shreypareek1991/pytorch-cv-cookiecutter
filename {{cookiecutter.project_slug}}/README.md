# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

A production-ready computer vision project powered by PyTorch, featuring modern tooling for development, training, and deployment.

## 🚀 Quick Start

```bash
# Navigate to project directory
cd {{ cookiecutter.project_slug }}

# Activate virtual environment
source .venv/bin/activate

# Or use uv directly (no activation needed)
uv run python scripts/train.py --help
```

## 📋 Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Development](#development)
- [Training & Deployment](#training--deployment)
- [Docker](#docker)
- [Experiment Tracking](#experiment-tracking)
- [Documentation](#documentation)

## Overview

This project provides a complete framework for computer vision tasks with:

- **PyTorch** for deep learning models
- **uv** for fast, reliable dependency management
- **Docker** support for both CUDA and CPU deployments
- **MLflow** integration for experiment tracking (optional)
- **Pre-commit hooks** for code quality
- **Comprehensive testing** with pytest

## Project Structure

## Project Structure

```
.
├── configs/                # Hydra/YAML configs for training & deployment
├── docker/                 # Dockerfiles, build & run scripts, OS package lists
├── docs/                   # How-to guides (remote repo, MLflow, Docker)
├── scripts/                # Entrypoints for training/inference/utilities
├── src/{{ cookiecutter.python_package }}/
│   ├── data/               # Dataset + datamodule helpers
│   ├── training/           # Lightning/Trainer orchestration
│   ├── deployment/         # Serving utilities / export logic
│   └── utils/              # Shared helpers (metrics, transforms, etc.)
└── tests/                  # Pytest-based smoke & regression tests
```

## Getting Started

### Prerequisites

- Python {{ cookiecutter.python_version }} or higher
- `uv` CLI installed ([installation guide](https://docs.astral.sh/uv/))
- Docker (optional, for containerized deployment)
- NVIDIA Container Toolkit (optional, for CUDA support)

### Installation

If dependencies weren't automatically installed during project generation:

```bash
# Install all dependencies (including dev tools)
uv sync --all-extras

# Or install specific groups
uv sync --extra dev      # Development tools
uv sync --extra deploy   # Deployment dependencies
uv sync --extra ml       # MLflow (if enabled)
```

### Environment Management (uv)

- **Sync dependencies**: `uv sync`
- **Run scripts**: `uv run python scripts/train.py`
- **Add packages**: `uv add package-name`
- **Add dev tools**: `uv add --dev ruff`
- **Export lockfile**: `uv lock` (for CI/CD)

## Development

### Code Quality

This project uses pre-commit hooks to maintain code quality:

**Setup:**
```bash
make dev  # Installs pre-commit hooks
# Or manually: uv run pre-commit install
```

**Available Commands:**
```bash
make format      # Format code (black, isort, ruff)
make lint        # Lint code (ruff, mypy)
make test        # Run tests
make pre-commit  # Run all pre-commit checks manually
```

**Hooks included:**
- **Black**: Code formatting
- **isort**: Import sorting (black-compatible)
- **Ruff**: Fast linting and formatting
- **MyPy**: Type checking
- **Bandit**: Security vulnerability scanning
- **Pytest**: Runs tests on pre-push
- **File checks**: Trailing whitespace, YAML/TOML/JSON validation, etc.

Hooks run automatically on `git commit` and `git push`. To run manually:

```bash
# Run on all files
uv run pre-commit run --all-files

# Run on staged files only
git commit -m "your message"  # Hooks run automatically

# Run pre-push hooks manually
uv run pre-commit run --hook-stage pre-push
```

## Training & Deployment

### Training

Train your models using the provided training script:

```bash
# Basic training
uv run python scripts/train.py

# With custom config
uv run python scripts/train.py --config configs/training.yaml

# See all options
uv run python scripts/train.py --help
```

**Key Scripts:**
- `scripts/train.py`: Main training loop with configurable trainer/device
- `scripts/export.py`: Export models for deployment (TorchScript/ONNX)
- `scripts/serve.py`: FastAPI microservice for inference

**Configuration:**
- Training configs: `configs/training.yaml`
- Model configs: `configs/model.yaml`
- Deployment configs: `configs/deployment.yaml`
- Environment variables: `.env` (see `.env.example`)

### Model Export

Export trained models for deployment:

```bash
uv run python scripts/export.py --checkpoint path/to/checkpoint.ckpt --format onnx
```

### Serving

Start a FastAPI inference server:

```bash
uv run python scripts/serve.py --model path/to/model.pt
```

## Docker

### Quick Start

```bash
# Build Docker image
make docker-build

# Build CPU-only image (recommended for ARM Macs)
make docker-build-cpu

# Build and scan for vulnerabilities
make docker-build-scan

# Run container
make docker-run
```

### Dockerfiles

- **`docker/Dockerfile`**: CUDA-enabled image (default)
  - Base: `nvidia/cuda:{{ cookiecutter.cuda_version }}-cudnn8-runtime-ubuntu{{ cookiecutter.base_ubuntu_version }}`
  - Best for: Linux systems with NVIDIA GPUs (x86_64)
  - Note: Automatically switches to CPU Dockerfile on ARM Macs

- **`docker/Dockerfile.cpu`**: CPU-only image
  - Base: `python:{{ cookiecutter.python_version }}-slim`
  - Best for: ARM Macs, CPU-only deployments, CI/CD

### Building Images

```bash
# Using make
make docker-build              # Build default (auto-switches to CPU on ARM)
make docker-build-cpu          # Build CPU image explicitly
make docker-build-cuda         # Build CUDA image (x86_64 Linux only)
make docker-build-scan         # Build and scan

# Using scripts directly
bash docker/build.sh           # Default build
bash docker/build.sh --cpu     # Force CPU build
bash docker/build.sh --scan    # Build and scan
```

### Running Containers

```bash
# Using make
make docker-run

# Using scripts
bash docker/run.sh

# Manual run
docker run -it --gpus all {{ cookiecutter.docker_image_name }}
```

### Vulnerability Scanning

Scan Docker images for security vulnerabilities:

```bash
# Scan existing image
make docker-scan

# Or using script
bash docker/scan.sh --image {{ cookiecutter.docker_image_name }}

# Build and scan in one step
make docker-build-scan
```

**Note:** On ARM Macs, the build script automatically uses the CPU Dockerfile since CUDA images don't run natively on ARM.

See `docs/docker.md` for detailed Docker documentation.

## Experiment Tracking

{% if cookiecutter.enable_mlflow_tracking == "y" or cookiecutter.enable_mlflow_tracking == "yes" %}
This project uses **MLflow** for experiment tracking.

### Starting MLflow Server

```bash
# Using Docker Compose (recommended)
cd mlflow
docker-compose up -d

# Access UI at http://localhost:5000
```

### Configuration

- **Backend store**: `{{ cookiecutter.mlflow_backend_store }}`
- **Artifact root**: `{{ cookiecutter.mlflow_artifact_root }}`
- **Tracking URI**: Configured in `configs/tracking.yaml`

### Usage

The training script automatically logs to MLflow. View experiments at:
- Local: http://localhost:5000
- Remote: Configure in `configs/tracking.yaml`

See `docs/mlflow.md` for detailed setup and usage instructions.
{% else %}
MLflow tracking is not enabled for this project. To enable it, you would need to:
1. Set up MLflow server
2. Configure tracking URI in `configs/tracking.yaml`
3. Update training scripts to log metrics
{% endif %}

## Documentation

Comprehensive documentation is available in the `docs/` directory:

- **`docs/docker.md`**: Docker usage, building, running, and vulnerability scanning
- **`docs/remote_repo.md`**: Setting up remote Git repositories
{% if cookiecutter.enable_mlflow_tracking == "y" or cookiecutter.enable_mlflow_tracking == "yes" %}
- **`docs/mlflow.md`**: MLflow setup and experiment tracking
{% endif %}

## Git & Remote Repository

### Initial Setup

Git is already initialized. To connect to a remote repository:

```bash
# Add remote repository
git remote add origin <REMOTE_URL>

# Push to remote
git push -u origin main
```

### Remote Repository Options

1. **GitHub**: Create a new repository and use the provided URL
2. **GitLab**: Similar process, use GitLab repository URL
3. **Other**: Any Git-compatible remote works

See `docs/remote_repo.md` for detailed instructions including:
- SSH vs HTTPS setup
- Personal Access Tokens (PAT)
- Multiple remote configurations
- Protected branches and CI/CD setup

## Common Tasks

### Running Tests

```bash
# Run all tests
make test
# or
uv run pytest

# Run specific test file
uv run pytest tests/test_model.py

# Run with coverage
uv run pytest --cov=src
```

### Code Formatting

```bash
# Format all code
make format

# Check formatting without changes
uv run black --check .
uv run isort --check-only .
```

### Linting

```bash
# Run all linters
make lint

# Individual tools
uv run ruff check .
uv run mypy src/
uv run bandit -r src/
```

### Adding Dependencies

```bash
# Add runtime dependency
uv add package-name

# Add dev dependency
uv add --dev package-name

# Add to specific extra
uv add --extra deploy package-name
```

## Troubleshooting

### Common Issues

**Issue**: `uv sync` fails
- **Solution**: Ensure Python {{ cookiecutter.python_version }} is installed and `uv` is up to date

**Issue**: Docker build fails on ARM Mac
- **Solution**: Use `make docker-build-cpu` or `bash docker/build.sh --cpu`

**Issue**: CUDA not available
- **Solution**: Use CPU Dockerfile or ensure NVIDIA drivers are installed

**Issue**: Pre-commit hooks fail
- **Solution**: Run `make format` to auto-fix formatting issues, then commit again

## Project Information

- **Author**: {{ cookiecutter.full_name }}
- **Organization**: {{ cookiecutter.organization }}
- **Email**: {{ cookiecutter.email }}
- **Python Version**: {{ cookiecutter.python_version }}
- **Default Device**: {{ cookiecutter.default_device }}

## Next Steps

1. ✅ Review this README
2. ✅ Set up environment: `uv sync --all-extras`
3. ✅ Install pre-commit hooks: `make dev`
4. ✅ Run tests: `make test`
5. ✅ Configure `.env` file (see `.env.example`)
6. ✅ Update `configs/*.yaml` with your data sources
7. ✅ Set up remote repository (see `docs/remote_repo.md`)
8. ✅ Start developing!

## Support

For issues, questions, or contributions:
- Check existing documentation in `docs/`
- Review code comments and docstrings
- Open an issue in the repository (if applicable)

---

**Happy building! 🚀**

