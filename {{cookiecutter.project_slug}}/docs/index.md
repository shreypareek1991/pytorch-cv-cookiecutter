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

## ✨ Features

- **PyTorch** for deep learning models
- **FastAPI** for REST API with OpenAPI/Swagger documentation
- **uv** for fast, reliable dependency management
- **Docker** support for both CUDA and CPU deployments
{% if cookiecutter.enable_mlflow_tracking == "y" or cookiecutter.enable_mlflow_tracking == "yes" %}
- **MLflow** integration for experiment tracking
{% endif %}
- **Pre-commit hooks** for code quality
- **Comprehensive testing** with pytest
- **MkDocs** documentation website

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
├── docker/               # Docker files
├── docs/                 # Documentation
└── tests/                # Test files
```

## 📚 Documentation

This documentation covers all aspects of the project:

- **[Getting Started](GETTING_STARTED.md)** - Installation, prerequisites, and environment setup
- **[Development Guide](DEVELOPMENT.md)** - Code quality, testing, and development workflow
- **[API Documentation](../app/README.md)** - FastAPI application guide and usage
- **[Docker Guide](docker.md)** - Docker usage, building, and vulnerability scanning
{% if cookiecutter.enable_mlflow_tracking == "y" or cookiecutter.enable_mlflow_tracking == "yes" %}
- **[MLflow Tracking](mlflow.md)** - Experiment tracking setup
{% endif %}
- **[Remote Repository](remote_repo.md)** - Git remote configuration
- **[Troubleshooting](TROUBLESHOOTING.md)** - Common issues and solutions
- **[Quick Reference](QUICK_REFERENCE.md)** - Common commands and tasks

## 🎯 Getting Started

1. **Install dependencies**: `uv sync --all-extras`
2. **Run tests**: `make test`
3. **Install pre-commit hooks**: `make dev`
4. **Start the API**: `make app`

See the [Getting Started Guide](GETTING_STARTED.md) for detailed setup instructions.

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

## 🏗️ Architecture

### API Application

The project uses FastAPI for the REST API:

1. **API Routes**: Defined in `app/main.py`
2. **Vision Utilities**: Computer vision functions in `{{ cookiecutter.python_package }}/vision.py`
3. **OpenAPI Documentation**: Automatically generated at `/docs`

### Configuration

Configuration is managed through YAML files:

- `configs/deployment.yaml` - API server configuration

## 🔧 Development

The project uses modern Python development tools:

- **Pre-commit hooks** for automatic code quality checks
- **Black** and **isort** for code formatting
- **Ruff** for fast linting
- **MyPy** for type checking
- **Pytest** for testing

See the [Development Guide](DEVELOPMENT.md) for more details.

## 🐳 Docker

Docker images are available for both CUDA and CPU deployments:

- **CUDA image**: For GPU-accelerated inference
- **CPU image**: For ARM Macs and CPU-only deployments

See the [Docker Guide](docker.md) for detailed instructions.

## 📊 Experiment Tracking

{% if cookiecutter.enable_mlflow_tracking == "y" or cookiecutter.enable_mlflow_tracking == "yes" %}
This project uses **MLflow** for experiment tracking. Track metrics, parameters, and artifacts during model development.

See the [MLflow Guide](mlflow.md) for setup and usage.
{% else %}
MLflow tracking is not enabled. You can enable it by configuring MLflow in your project.
{% endif %}

## 📝 Project Information

- **Author**: {{ cookiecutter.full_name }}
- **Organization**: {{ cookiecutter.organization }}
- **Email**: {{ cookiecutter.email }}
- **Python Version**: {{ cookiecutter.python_version }}
- **Default Device**: {{ cookiecutter.default_device }}

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linting: `make test && make lint`
5. Submit a pull request

See [CONTRIBUTING.md](../CONTRIBUTING.md) for more details.

## 📄 License

This project is licensed under the MIT License.

---

**Happy building! 🚀**
