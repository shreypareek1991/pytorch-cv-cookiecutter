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

## ✨ Features

- **PyTorch** for deep learning models
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

## 📚 Documentation

This documentation covers all aspects of the project:

- **[Getting Started](GETTING_STARTED.md)** - Installation, prerequisites, and environment setup
- **[Development Guide](DEVELOPMENT.md)** - Code quality, testing, and development workflow
- **[Training & Deployment](TRAINING.md)** - Model training, export, and serving
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
4. **Start training**: `uv run python scripts/train.py`

See the [Getting Started Guide](GETTING_STARTED.md) for detailed setup instructions.

## 📦 Quick Commands

```bash
make sync              # Sync all dependencies
make dev               # Install pre-commit hooks
make test              # Run tests
make format            # Format code
make lint              # Lint code
make docker-build      # Build Docker image
make docs              # Serve documentation website
```

## 🏗️ Architecture

### Training Pipeline

The project follows a modular architecture:

1. **Data Loading**: Dataset classes and data modules in `src/{{ cookiecutter.python_package }}/data/`
2. **Model Definition**: Model architectures in `src/{{ cookiecutter.python_package }}/training/`
3. **Training Loop**: Configurable training scripts in `scripts/train.py`
4. **Export & Serve**: Model export and serving utilities in `scripts/`

### Configuration

Configuration is managed through YAML files:

- `configs/training.yaml` - Training hyperparameters
- `configs/model.yaml` - Model architecture
- `configs/deployment.yaml` - Deployment settings

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

- **CUDA image**: For GPU-accelerated training and inference
- **CPU image**: For ARM Macs and CPU-only deployments

See the [Docker Guide](docker.md) for detailed instructions.

## 📊 Experiment Tracking

{% if cookiecutter.enable_mlflow_tracking == "y" or cookiecutter.enable_mlflow_tracking == "yes" %}
This project uses **MLflow** for experiment tracking. Track metrics, parameters, and artifacts during training.

See the [MLflow Guide](mlflow.md) for setup and usage.
{% else %}
MLflow tracking is not enabled. See the [Training Guide](TRAINING.md) to enable it.
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

## 📄 License

This project is licensed under the MIT License.

---

**Happy building! 🚀**

