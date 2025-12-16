# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

A production-ready computer vision project powered by PyTorch, featuring modern tooling for development and API deployment.

## 🚀 Quick Start

```bash
# Navigate to project directory
cd {{ cookiecutter.project_slug }}

# Sync dependencies
make sync

# Run the API application
make app
```

The API will be available at:
- **API**: http://localhost:8080
- **Swagger UI**: http://localhost:8080/docs
- **ReDoc**: http://localhost:8080/redoc

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
- **[API Documentation](app/README.md)** - FastAPI application guide and usage
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
├── docker/               # Dockerfiles and scripts
├── docs/                 # Documentation files
├── tests/                # Test files
└── pyproject.toml        # Project configuration
```

## 🎯 Overview

This project provides a complete framework for computer vision tasks with:

- **PyTorch** for deep learning models
- **FastAPI** for REST API with OpenAPI/Swagger documentation
- **uv** for fast, reliable dependency management
- **Docker** support for both CUDA and CPU deployments
- **Pre-commit hooks** for code quality
- **Comprehensive testing** with pytest

## 📦 Quick Commands

```bash
make sync              # Sync all dependencies
make dev               # Install pre-commit hooks
make test              # Run tests
make format            # Format code
make lint              # Lint code
make app               # Run FastAPI application
make docker build      # Build Docker image
make docs              # Serve documentation website
```

See [Quick Reference](docs/QUICK_REFERENCE.md) for all available commands.

## 🏃 Next Steps

1. Read [Getting Started](docs/GETTING_STARTED.md) for installation
2. Review [Development Guide](docs/DEVELOPMENT.md) for workflow
3. Check [API Documentation](app/README.md) to understand the API
4. Set up remote repository (see [Remote Repo Guide](docs/remote_repo.md))

## 📝 Project Information

- **Author**: {{ cookiecutter.full_name }}
- **Organization**: {{ cookiecutter.organization }}
- **Email**: {{ cookiecutter.email }}
- **Python Version**: {{ cookiecutter.python_version }}
- **Default Device**: {{ cookiecutter.default_device }}

---

**Happy building! 🚀**
