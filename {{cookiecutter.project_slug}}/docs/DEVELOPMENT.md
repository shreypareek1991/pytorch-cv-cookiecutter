# Development Guide

This guide covers development workflow, code quality, testing, and best practices.

## Code Quality

This project uses pre-commit hooks to maintain code quality automatically.

### Setup

```bash
# Install pre-commit hooks (one-time setup)
make dev
# or
uv run pre-commit install
```

### Available Commands

```bash
make format      # Format code (black, isort, ruff)
make lint        # Lint code (ruff, mypy)
make test        # Run tests
make pre-commit  # Run all pre-commit checks manually
```

### Pre-commit Hooks

The following hooks are configured:

- **Black**: Code formatting
- **isort**: Import sorting (black-compatible)
- **Ruff**: Fast linting and formatting
- **MyPy**: Type checking
- **Bandit**: Security vulnerability scanning
- **Pytest**: Runs tests on pre-push
- **File checks**: Trailing whitespace, YAML/TOML/JSON validation, etc.

### Usage

Hooks run automatically on `git commit` and `git push`:

```bash
# Hooks run automatically on commit
git commit -m "your message"

# Run hooks manually on all files
uv run pre-commit run --all-files

# Run pre-push hooks manually
uv run pre-commit run --hook-stage pre-push
```

## Testing

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

# Run specific test
uv run pytest tests/test_model.py::test_specific_function
```

### Writing Tests

- Place tests in the `tests/` directory
- Follow pytest conventions
- Use descriptive test names
- Group related tests in classes if needed

Example:
```python
def test_model_forward():
    model = MyModel()
    output = model(input_tensor)
    assert output.shape == expected_shape
```

## Code Formatting

### Format Code

```bash
# Format all code
make format

# Format specific files
uv run black src/
uv run isort src/
uv run ruff format src/
```

### Check Formatting

```bash
# Check without making changes
uv run black --check .
uv run isort --check-only .
uv run ruff check .
```

## Linting

### Run Linters

```bash
# Run all linters
make lint

# Individual tools
uv run ruff check .        # Fast linting
uv run mypy src/          # Type checking
uv run bandit -r src/     # Security scanning
```

### Fix Linting Issues

Many linting issues can be auto-fixed:

```bash
# Auto-fix ruff issues
uv run ruff check --fix .

# Format with ruff
uv run ruff format .
```

## Adding Dependencies

### Runtime Dependencies

```bash
# Add a package
uv add package-name

# Add with version constraint
uv add "package-name>=1.0.0"
```

### Development Dependencies

```bash
# Add dev tool
uv add --dev package-name

# Add to specific extra
uv add --extra deploy package-name
```

### Updating Dependencies

```bash
# Update lockfile
uv lock

# Update specific package
uv add --upgrade package-name
```

## Git Workflow

### Pre-commit Checks

Before committing, ensure:

1. Code is formatted: `make format`
2. Tests pass: `make test`
3. Linting passes: `make lint`

Or let pre-commit hooks handle it automatically.

### Commit Messages

Follow conventional commit format:

- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation
- `refactor:` for code refactoring
- `test:` for tests
- `chore:` for maintenance

Example:
```bash
git commit -m "feat: add data augmentation pipeline"
```

## Project Structure

### Source Code Organization

```
src/{{ cookiecutter.python_package }}/
├── data/          # Data loading, preprocessing, datasets
├── training/      # Training loops, trainers, callbacks
├── deployment/    # Model export, serving, inference
└── utils/         # Shared utilities, helpers, metrics
```

### Configuration

- **Configs**: `configs/*.yaml` - Training, model, deployment configs
- **Environment**: `.env` - Secrets and environment-specific settings
- **Project config**: `pyproject.toml` - Project metadata and tool configs

## Best Practices

1. **Type Hints**: Use type hints for better code clarity and IDE support
2. **Docstrings**: Document functions and classes
3. **Tests**: Write tests for new features
4. **Formatting**: Let pre-commit hooks format your code
5. **Linting**: Fix linting issues before committing
6. **Dependencies**: Keep dependencies up to date

## IDE Setup

### VS Code

Recommended extensions:
- Python
- Pylance
- Black Formatter
- Ruff

### PyCharm

- Enable Black as formatter
- Configure Ruff as external tool
- Enable type checking with MyPy

## Next Steps

- Review [Training Guide](TRAINING.md) for model development
- Check [Quick Reference](QUICK_REFERENCE.md) for common commands
- See [Troubleshooting](TROUBLESHOOTING.md) for common issues

