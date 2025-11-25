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

## 📚 Documentation

### 📖 Documentation Website

View the full documentation website:

```bash
# Serve documentation locally
make docs
# or
uv run mkdocs serve
```

Then open http://127.0.0.1:8000 in your browser.

### 📄 Documentation Files

- **[Getting Started](docs/GETTING_STARTED.md)** - Installation, prerequisites, and environment setup
- **[Development Guide](docs/DEVELOPMENT.md)** - Code quality, testing, and development workflow
- **[Training & Deployment](docs/TRAINING.md)** - Model training, export, and serving
- **[Docker Guide](docs/docker.md)** - Docker usage, building, and vulnerability scanning
- **[Troubleshooting](docs/TROUBLESHOOTING.md)** - Common issues and solutions
- **[Quick Reference](docs/QUICK_REFERENCE.md)** - Common commands and tasks

{% if cookiecutter.enable_mlflow_tracking == "y" or cookiecutter.enable_mlflow_tracking == "yes" %}
- **[MLflow Tracking](docs/mlflow.md)** - Experiment tracking setup
{% endif %}
- **[Remote Repository](docs/remote_repo.md)** - Git remote configuration

## 📋 Project Structure

```
.
├── configs/                # Hydra/YAML configs for training & deployment
├── docker/                 # Dockerfiles, build & run scripts, OS package lists
├── docs/                   # Documentation files
├── scripts/                # Entrypoints for training/inference/utilities
├── src/{{ cookiecutter.python_package }}/
│   ├── data/               # Dataset + datamodule helpers
│   ├── training/           # Lightning/Trainer orchestration
│   ├── deployment/         # Serving utilities / export logic
│   └── utils/              # Shared helpers (metrics, transforms, etc.)
└── tests/                  # Pytest-based smoke & regression tests
```

## 🎯 Overview

This project provides a complete framework for computer vision tasks with:

- **PyTorch** for deep learning models
- **uv** for fast, reliable dependency management
- **Docker** support for both CUDA and CPU deployments
- **MLflow** integration for experiment tracking (optional)
- **Pre-commit hooks** for code quality
- **Comprehensive testing** with pytest

## 📦 Quick Commands

```bash
make sync              # Sync all dependencies
make dev               # Install pre-commit hooks
make test              # Run tests
make format            # Format code
make lint              # Lint code
make docker-build      # Build Docker image
make docs               # Serve documentation website
```

See [Quick Reference](docs/QUICK_REFERENCE.md) for all available commands.

## 🏃 Next Steps

1. Read [Getting Started](docs/GETTING_STARTED.md) for installation
2. Review [Development Guide](docs/DEVELOPMENT.md) for workflow
3. Check [Training Guide](docs/TRAINING.md) to start training models
4. Set up remote repository (see [Remote Repo Guide](docs/remote_repo.md))

## 📝 Project Information

- **Author**: {{ cookiecutter.full_name }}
- **Organization**: {{ cookiecutter.organization }}
- **Email**: {{ cookiecutter.email }}
- **Python Version**: {{ cookiecutter.python_version }}
- **Default Device**: {{ cookiecutter.default_device }}

---

**Happy building! 🚀**
