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
# Format code
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

## Training Commands

```bash
# Basic training
uv run python scripts/train.py

# With custom config
uv run python scripts/train.py --config configs/training.yaml

# Export model
uv run python scripts/export.py --checkpoint model.ckpt --format onnx

# Start inference server
uv run python scripts/serve.py --model model.pt
```

## Documentation Commands

```bash
# Serve documentation website
make docs

# Build documentation
make docs-build

# Or using mkdocs directly
uv run mkdocs serve
uv run mkdocs build
```

## Docker Commands

```bash
# Build image
make docker-build

# Build CPU image
make docker-build-cpu

# Build and scan
make docker-build-scan

# Run container
make docker-run

# Scan image
make docker-scan
```

## Testing Commands

```bash
# Run all tests
uv run pytest

# Run specific test file
uv run pytest tests/test_model.py

# Run with coverage
uv run pytest --cov=src

# Run specific test
uv run pytest tests/test_model.py::test_function
```

## Code Quality Commands

```bash
# Format with black
uv run black src/

# Sort imports
uv run isort src/

# Lint with ruff
uv run ruff check src/

# Type check
uv run mypy src/

# Security scan
uv run bandit -r src/
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
├── configs/          # Configuration files
├── docker/           # Docker files
├── docs/             # Documentation
├── scripts/          # Entrypoint scripts
├── src/              # Source code
└── tests/            # Test files
```

## Configuration Files

- `configs/training.yaml` - Training configuration
- `configs/model.yaml` - Model configuration
- `configs/deployment.yaml` - Deployment configuration
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

### Running training

```bash
# 1. Configure training
# Edit configs/training.yaml

# 2. Start training
uv run python scripts/train.py

# 3. Monitor (if MLflow enabled)
# Open http://localhost:5000
```

### Deploying model

```bash
# 1. Export model
uv run python scripts/export.py --checkpoint model.ckpt --format onnx

# 2. Build Docker image
make docker-build

# 3. Run container
make docker-run
```

## Make Targets

```bash
make sync              # Sync dependencies
make dev               # Install pre-commit hooks
make test              # Run tests
make format            # Format code
make lint              # Lint code
make pre-commit        # Run pre-commit checks
make docker-build      # Build Docker image
make docker-build-cpu  # Build CPU image
make docker-build-scan # Build and scan
make docker-run        # Run container
make docker-scan       # Scan image
```

## Environment Variables

Common environment variables (set in `.env`):

- `MLFLOW_TRACKING_URI` - MLflow server URI
- `CUDA_VISIBLE_DEVICES` - GPU selection
- `PYTHONPATH` - Python path (usually not needed)

## Useful Links

- [Getting Started](GETTING_STARTED.md) - Setup and installation
- [Development Guide](DEVELOPMENT.md) - Development workflow
- [Training Guide](TRAINING.md) - Model training
- [Docker Guide](docker.md) - Docker usage
- [Troubleshooting](TROUBLESHOOTING.md) - Common issues

