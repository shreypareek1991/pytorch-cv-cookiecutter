# Quick Reference

Quick lookup for common commands and tasks.

## Environment Management

```bash
# Sync all dependencies
uv sync --all-extras

# Sync specific extras
uv sync --extra dev
uv sync --extra deploy

# Add dependency
uv add package-name

# Add dev dependency
uv add --dev package-name

# Update lockfile
uv lock
```

## Development Commands

```bash
# Format code (including science folder)
make format

# Lint code
make lint

# Run tests
make test

# Install pre-commit hooks
make dev

# Run pre-commit checks
make pre-commit
```

## API Application Commands

```bash
# Run FastAPI application (development)
make app
# or
make app serve

# Using uvicorn directly
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8080

# Production mode
uv run uvicorn app.main:app --host 0.0.0.0 --port 8080 --workers 4
```

## Documentation Commands

```bash
# Serve documentation website
make docs
# or
make docs serve

# Build documentation
make docs build

# Or using mkdocs directly
uv run mkdocs serve
uv run mkdocs build
```

## Docker Commands

```bash
# Build image (auto-switches to CPU on ARM)
make docker build

# Build CPU image
make docker build-cpu

# Build CUDA image (x86_64 Linux only)
make docker build-cuda

# Build and scan
make docker build-scan

# Run container
make docker run

# Scan image
make docker scan
```

## Testing Commands

```bash
# Run all tests
uv run pytest

# Run specific test file
uv run pytest tests/test_imports.py

# Run with coverage
uv run pytest --cov={{ cookiecutter.python_package }} --cov=app

# Run specific test
uv run pytest tests/test_imports.py::test_package_import
```

## Code Quality Commands

```bash
# Format with black (including science folder)
uv run black {{ cookiecutter.python_package }} app tests science

# Sort imports (excludes science folder)
uv run isort {{ cookiecutter.python_package }} app tests

# Lint with ruff (excludes science folder)
uv run ruff check {{ cookiecutter.python_package }} app tests

# Type check (excludes science folder)
uv run mypy {{ cookiecutter.python_package }} app

# Security scan (excludes science folder)
uv run bandit -r {{ cookiecutter.python_package }}/,app/
```

## Git Commands

```bash
# Initialize (already done)
git init

# Add remote
git remote add origin <URL>

# Push to remote
git push -u origin main

# Commit (hooks run automatically)
git commit -m "message"
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
├── docker/               # Docker files
├── docs/                 # Documentation
└── tests/                # Test files
```

## Configuration Files

- `configs/deployment.yaml` - API deployment configuration
- `.env` - Environment variables (copy from `.env.example`)
- `pyproject.toml` - Project configuration

## Common Workflows

### Starting a new feature

```bash
# 1. Sync dependencies
uv sync --all-extras

# 2. Create branch
git checkout -b feature/my-feature

# 3. Make changes
# ... edit code ...

# 4. Format and test
make format
make test

# 5. Commit (hooks run automatically)
git commit -m "feat: add new feature"
```

### Running the API

```bash
# 1. Start the API server
make app

# 2. Test the API
# Open http://localhost:8080/docs in browser
# Or use curl:
curl http://localhost:8080/health

# 3. Make a prediction
curl -X POST "http://localhost:8080/predict" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@path/to/image.jpg"
```

### Deploying with Docker

```bash
# 1. Build Docker image
make docker build

# 2. Run container
make docker run

# 3. Test API
curl http://localhost:8080/health
```

## Make Targets

```bash
make sync              # Sync dependencies
make dev               # Install pre-commit hooks
make test              # Run tests
make format            # Format code
make lint              # Lint code
make pre-commit        # Run pre-commit checks
make app               # Run FastAPI application
make docker build      # Build Docker image
make docker build-cpu  # Build CPU image
make docker build-cuda # Build CUDA image
make docker build-scan # Build and scan
make docker run        # Run container
make docker scan       # Scan image
make docs              # Serve documentation
make docs build        # Build documentation
```

## Environment Variables

Common environment variables (set in `.env`):

- `API_HOST` - API host (default: 0.0.0.0)
- `API_PORT` - API port (default: 8080)
- `CUDA_VISIBLE_DEVICES` - GPU selection
- `PYTHONPATH` - Python path (usually not needed)

## Useful Links

- [Getting Started](GETTING_STARTED.md) - Setup and installation
- [Development Guide](DEVELOPMENT.md) - Development workflow
- [API Documentation](../app/README.md) - FastAPI application guide
- [Docker Guide](docker.md) - Docker usage
- [Troubleshooting](TROUBLESHOOTING.md) - Common issues
