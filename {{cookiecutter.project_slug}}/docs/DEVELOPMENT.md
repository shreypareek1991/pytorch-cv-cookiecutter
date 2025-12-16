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

- **Black**: Code formatting (includes science folder)
- **isort**: Import sorting (black-compatible, excludes science folder)
- **Ruff**: Fast linting and formatting (excludes science folder)
- **MyPy**: Type checking (excludes science folder)
- **Bandit**: Security vulnerability scanning (excludes science folder)
- **Pytest**: Runs tests on pre-push
- **File checks**: Trailing whitespace, YAML/TOML/JSON validation, etc.

**Note**: The `science/` folder is excluded from most pre-commit hooks (except black formatting) to allow flexibility for data science work. However, it's recommended to format notebooks and Python files in the science folder using black.

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
uv run pytest tests/test_imports.py

# Run with coverage
uv run pytest --cov={{ cookiecutter.python_package }} --cov=app

# Run specific test
uv run pytest tests/test_imports.py::test_package_import
```

### Writing Tests

- Place tests in the `tests/` directory
- Follow pytest conventions
- Use descriptive test names
- Group related tests in classes if needed

Example:
```python
def test_vision_utils():
    from {{ cookiecutter.python_package }}.vision import load_image
    # Test implementation
    assert True
```

## Code Formatting

### Format Code

```bash
# Format all code (including science folder)
make format

# Format specific files
uv run black {{ cookiecutter.python_package }} app tests science
uv run isort {{ cookiecutter.python_package }} app tests
uv run ruff format {{ cookiecutter.python_package }} app tests
```

### Check Formatting

```bash
# Check without making changes
uv run black --check {{ cookiecutter.python_package }} app tests
uv run isort --check-only {{ cookiecutter.python_package }} app tests
uv run ruff check {{ cookiecutter.python_package }} app tests
```

## Linting

### Run Linters

```bash
# Run all linters
make lint

# Individual tools
uv run ruff check {{ cookiecutter.python_package }} app tests        # Fast linting
uv run mypy {{ cookiecutter.python_package }} app          # Type checking
uv run bandit -r {{ cookiecutter.python_package }}/,app/     # Security scanning
```

### Fix Linting Issues

Many linting issues can be auto-fixed:

```bash
# Auto-fix ruff issues
uv run ruff check --fix {{ cookiecutter.python_package }} app tests

# Format with ruff
uv run ruff format {{ cookiecutter.python_package }} app tests
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

### Update Dependencies

```bash
# Update all dependencies
uv lock --upgrade

# Update specific package
uv lock --upgrade-package package-name
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

## Science Folder

The `science/` folder is for data science work and is excluded from most pre-commit hooks:

- **`science/data/`** - Store data files here (gitignored)
- **`science/models/`** - Store trained models here (gitignored)
- **`science/notebooks/`** - Jupyter notebooks for exploration

**Note**: While pre-commit hooks don't enforce code quality in the science folder, it's still recommended to:
- Format Python files and notebooks with black
- Keep notebooks organized and documented
- Use meaningful variable names

You can format the science folder manually:
```bash
uv run black science/
```

## Type Checking

Type checking is performed with MyPy:

```bash
# Run type checking
uv run mypy {{ cookiecutter.python_package }} app

# Check specific file
uv run mypy {{ cookiecutter.python_package }}/vision.py
```

The project uses type hints where possible. Add type annotations to new code:

```python
from typing import Any

def process_image(image_path: str) -> dict[str, Any]:
    """Process an image and return results."""
    # Implementation
    return {}
```

## Security Scanning

Security vulnerabilities are checked with Bandit:

```bash
# Run security scan
uv run bandit -r {{ cookiecutter.python_package }}/,app/

# With specific severity level
uv run bandit -r {{ cookiecutter.python_package }}/,app/ -ll  # Low/Medium
```

## Best Practices

1. **Write tests** for new functionality
2. **Use type hints** for better code clarity
3. **Format code** before committing (hooks do this automatically)
4. **Keep functions small** and focused
5. **Document complex logic** with docstrings
6. **Follow PEP 8** style guidelines (enforced by tools)

## Common Issues

**Issue**: Pre-commit hooks fail
- **Solution**: Run `make format` and `make lint` to fix issues, then commit again

**Issue**: Type checking errors
- **Solution**: Add type hints or use `# type: ignore` comments for third-party code

**Issue**: Tests fail
- **Solution**: Check test output, fix failing tests, ensure dependencies are installed

See [Troubleshooting](TROUBLESHOOTING.md) for more help.
