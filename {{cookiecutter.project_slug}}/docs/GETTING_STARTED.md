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
uv sync --extra deploy   # Deployment dependencies (FastAPI, uvicorn)
{% if cookiecutter.enable_mlflow_tracking == "y" or cookiecutter.enable_mlflow_tracking == "yes" %}
uv sync --extra ml       # MLflow (if enabled)
{% endif %}
{% if cookiecutter.enable_dvc == "y" or cookiecutter.enable_dvc == "yes" %}
uv sync --extra dvc      # DVC (if enabled)
{% endif %}
```

## Environment Management (uv)

The project uses `uv` for fast, reliable dependency management:

### Basic Commands

- **Sync dependencies**: `uv sync`
- **Run Python scripts**: `uv run python app/main.py`
- **Add packages**: `uv add package-name`
- **Add dev tools**: `uv add --dev ruff`
- **Export lockfile**: `uv lock` (for CI/CD)

### Virtual Environment

`uv` automatically manages a virtual environment in `.venv/`. You can:

```bash
# Activate the virtual environment (optional)
source .venv/bin/activate

# Or use uv directly (no activation needed)
uv run python app/main.py
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

# Start the API application
make app
# The API will be available at http://localhost:8080
# Swagger UI at http://localhost:8080/docs
```

## Project Structure

```
.
├── {{ cookiecutter.python_package }}/    # Main Python package
│   ├── vision.py         # Computer vision utilities
│   └── utils/            # Utility functions
├── app/                  # FastAPI application
│   ├── main.py          # API routes and server
│   └── README.md        # API documentation
├── science/              # Data science work
│   ├── data/            # Data files (gitignored)
│   ├── models/          # Trained models (gitignored)
│   └── notebooks/       # Jupyter notebooks
├── configs/              # Configuration files
├── docker/               # Dockerfiles and build scripts
├── docs/                 # Documentation
└── tests/                # Test files
```

## Configuration Files

- **Deployment configs**: `configs/deployment.yaml` - API server configuration
- **Environment variables**: `.env` (copy from `.env.example`)

## Running the API

Start the FastAPI application:

```bash
# Development mode (with auto-reload)
make app

# Or using uvicorn directly
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8080
```

The API will be available at:
- **API**: http://localhost:8080
- **Swagger UI**: http://localhost:8080/docs
- **ReDoc**: http://localhost:8080/redoc

See [API Documentation](../app/README.md) for more details.

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
make docs build
# or
uv run mkdocs build
```

The built site will be in the `site/` directory.

## Science Folder

The `science/` folder is for data science work:

- **`science/data/`** - Store your data files here (gitignored)
- **`science/models/`** - Store trained models here (gitignored)
- **`science/notebooks/`** - Jupyter notebooks for exploration

Note: Code in the `science/` folder is excluded from pre-commit hooks (except black formatting which is helpful).

## Next Steps

1. ✅ Install dependencies (if not done automatically)
2. ✅ Run tests: `make test`
3. ✅ Install pre-commit hooks: `make dev`
4. ✅ Configure `.env` file (see `.env.example`)
5. ✅ Start the API: `make app`
6. ✅ Review [Development Guide](DEVELOPMENT.md)
7. ✅ Check [API Documentation](../app/README.md)
8. ✅ View documentation website: `make docs`

## Common Issues

**Issue**: `uv sync` fails
- **Solution**: Ensure Python {{ cookiecutter.python_version }} is installed and `uv` is up to date

**Issue**: Command not found: `uv`
- **Solution**: Install `uv` from [https://docs.astral.sh/uv/](https://docs.astral.sh/uv/)

**Issue**: API not starting
- **Solution**: Check that port 8080 is not in use, or change the port in `app/main.py`

See [Troubleshooting](TROUBLESHOOTING.md) for more help.
