# Getting Started

This guide will help you set up your development environment and get started with the project.

## Prerequisites

- Python {{ cookiecutter.python_version }} or higher
- `uv` CLI installed ([installation guide](https://docs.astral.sh/uv/))
- Docker (optional, for containerized deployment)
- NVIDIA Container Toolkit (optional, for CUDA support)

## Installation

### Automatic Installation

If you selected "yes" for automatic dependency installation during project generation, dependencies should already be installed. Skip to [Verification](#verification).

### Manual Installation

If dependencies weren't automatically installed:

```bash
# Install all dependencies (including dev tools)
uv sync --all-extras

# Or install specific groups
uv sync --extra dev      # Development tools
uv sync --extra deploy   # Deployment dependencies
{% if cookiecutter.enable_mlflow_tracking == "y" or cookiecutter.enable_mlflow_tracking == "yes" %}
uv sync --extra ml       # MLflow (if enabled)
{% endif %}
```

## Environment Management (uv)

The project uses `uv` for fast, reliable dependency management:

### Basic Commands

- **Sync dependencies**: `uv sync`
- **Run scripts**: `uv run python scripts/train.py`
- **Add packages**: `uv add package-name`
- **Add dev tools**: `uv add --dev ruff`
- **Export lockfile**: `uv lock` (for CI/CD)

### Virtual Environment

`uv` automatically manages a virtual environment in `.venv/`. You can:

```bash
# Activate the virtual environment (optional)
source .venv/bin/activate

# Or use uv directly (no activation needed)
uv run python scripts/train.py
```

## Verification

Verify your installation:

```bash
# Check Python version
uv run python --version

# Run tests
make test
# or
uv run pytest

# Check that scripts are available
uv run python scripts/train.py --help
```

## Project Structure

```
.
├── configs/                # Configuration files (YAML)
├── docker/                 # Dockerfiles and build scripts
├── docs/                   # Documentation
├── scripts/                # Entrypoint scripts
│   ├── train.py           # Training script
│   ├── export.py          # Model export
│   └── serve.py           # Inference server
├── src/{{ cookiecutter.python_package }}/
│   ├── data/              # Data loading and preprocessing
│   ├── training/         # Training logic
│   ├── deployment/       # Deployment utilities
│   └── utils/            # Shared utilities
└── tests/                # Test files
```

## Configuration Files

- **Training configs**: `configs/training.yaml`
- **Model configs**: `configs/model.yaml`
- **Deployment configs**: `configs/deployment.yaml`
- **Environment variables**: `.env` (copy from `.env.example`)

## Documentation Website

The project includes a documentation website built with MkDocs and Material theme:

```bash
# Serve documentation locally
make docs
# or
uv run mkdocs serve
```

Then open http://127.0.0.1:8000 in your browser.

To build static documentation:

```bash
make docs-build
# or
uv run mkdocs build
```

The built site will be in the `site/` directory.

## Next Steps

1. ✅ Install dependencies (if not done automatically)
2. ✅ Run tests: `make test`
3. ✅ Install pre-commit hooks: `make dev`
4. ✅ Configure `.env` file (see `.env.example`)
5. ✅ Review [Development Guide](DEVELOPMENT.md)
6. ✅ Check [Training Guide](TRAINING.md)
7. ✅ View documentation website: `make docs`

## Common Issues

**Issue**: `uv sync` fails
- **Solution**: Ensure Python {{ cookiecutter.python_version }} is installed and `uv` is up to date

**Issue**: Command not found: `uv`
- **Solution**: Install `uv` from [https://docs.astral.sh/uv/](https://docs.astral.sh/uv/)

See [Troubleshooting](TROUBLESHOOTING.md) for more help.

