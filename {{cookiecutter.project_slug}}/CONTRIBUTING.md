# Contributing to {{ cookiecutter.project_name }}

Thank you for your interest in contributing! This guide will help you get started with contributing to this project.

## Getting Started

### Prerequisites

- Python ≥ {{ cookiecutter.python_version }}
- `git` installed
- `uv` CLI installed (https://docs.astral.sh/uv/)

### Cloning the Repository

```bash
# Clone the repository
git clone <your-repo-url>
cd {{ cookiecutter.project_slug }}

# Or if you've already cloned it, update to latest
git pull origin main
```

### Setting Up Your Development Environment

1. **Install dependencies**:
   ```bash
   # Sync all dependencies including dev extras
   uv sync --all-extras
   
   # Activate the virtual environment
   source .venv/bin/activate  # On macOS/Linux
   # or
   .venv\Scripts\activate  # On Windows
   ```

2. **Install pre-commit hooks**:
   ```bash
   make dev
   # or
   pre-commit install
   ```

3. **Verify setup**:
   ```bash
   make test
   make lint
   ```

## Development Workflow

### Making Changes

1. **Create a branch**:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

2. **Make your changes**:
   - Write clean, well-documented code
   - Follow the project's code style (enforced by pre-commit hooks)
   - Add tests for new functionality
   - Update documentation as needed

3. **Test your changes**:
   ```bash
   # Run tests
   make test
   
   # Check formatting
   make format
   
   # Run linting
   make lint
   
   # Run all pre-commit checks manually
   make pre-commit
   ```

4. **Commit your changes**:
   ```bash
   git add .
   git commit -m "feat: add new feature description"
   ```

   **Commit message conventions:**
   - `feat:` for new features
   - `fix:` for bug fixes
   - `docs:` for documentation changes
   - `refactor:` for code refactoring
   - `test:` for test additions/changes
   - `chore:` for maintenance tasks

### Testing Your Changes

Before submitting a PR, ensure:

- ✅ All tests pass (`make test`)
- ✅ Code is properly formatted (`make format`)
- ✅ Linting passes (`make lint`)
- ✅ Type checking passes (included in `make lint`)
- ✅ Pre-commit hooks pass (`make pre-commit`)
- ✅ Documentation is updated if needed

## Submitting a Pull Request

### Before Submitting

1. **Update documentation** if your changes affect:
   - API or public interfaces
   - Configuration options
   - Dependencies or requirements
   - Usage instructions

2. **Test thoroughly**:
   - Test your changes locally
   - Verify existing functionality isn't broken
   - Check edge cases

3. **Keep PRs focused**:
   - One feature or fix per PR
   - Keep changes small and reviewable
   - Include clear description of what changed and why

### PR Process

1. **Push your branch**:
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create a Pull Request** on GitHub/GitLab:
   - Provide a clear title and description
   - Reference any related issues
   - Include examples or screenshots if applicable
   - List what you tested

3. **Respond to feedback**:
   - Address review comments promptly
   - Make requested changes
   - Update your branch as needed

### PR Checklist

- [ ] Changes tested locally
- [ ] All tests pass (`make test`)
- [ ] Code formatted (`make format`)
- [ ] Linting passes (`make lint`)
- [ ] Documentation updated (if needed)
- [ ] Commit messages follow conventions
- [ ] No breaking changes (or clearly documented)

## Code Style

This project uses automated code formatting and linting:

- **Black** for code formatting
- **isort** for import sorting
- **ruff** for linting
- **mypy** for type checking

All of these are enforced via pre-commit hooks. You can run them manually:

```bash
make format  # Format code
make lint    # Lint and type check
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
├── configs/               # Configuration files
│   └── deployment.yaml   # Deployment configuration
├── docker/                # Docker files
│   ├── Dockerfile        # CUDA Dockerfile
│   ├── Dockerfile.cpu    # CPU Dockerfile
│   ├── build.sh          # Build script
│   └── run.sh            # Run script
├── tests/                 # Test files
├── docs/                  # Documentation
├── pyproject.toml        # Project configuration
├── Makefile              # Common commands
└── README.md             # Project overview
```

## Common Contribution Areas

### Adding New Features

1. Add code to `src/{{ cookiecutter.python_package }}/`
2. Add tests to `tests/`
3. Update documentation in `docs/`
4. Add scripts to `scripts/` if needed
5. Update `README.md` if it affects usage

### Fixing Bugs

1. Reproduce the bug
2. Write a test that fails due to the bug
3. Fix the bug
4. Verify the test passes
5. Update documentation if needed

### Improving Documentation

- Update relevant files in `docs/`
- Update `README.md` for major changes
- Add docstrings to new functions/classes
- Update API documentation in `docs/API.md`

### Adding Dependencies

Update `pyproject.toml`:
- Add to `[project.dependencies]` for runtime deps
- Add to `[project.optional-dependencies.dev]` for dev tools
- Add to `[project.optional-dependencies.deploy]` for deployment
- Add to `[project.optional-dependencies.ml]` for ML-specific tools

Then run:
```bash
uv sync --all-extras
```

## Running Tests

```bash
# Run all tests
make test

# Run tests with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_specific.py

# Run tests in watch mode (if pytest-watch installed)
ptw
```

## Docker Development

```bash
# Build Docker image
make docker build

# Run Docker container
make docker run

# Build and scan for vulnerabilities
make docker build-scan
```

See `docs/docker.md` for more details.

## Questions?

- Open an issue for bugs or feature requests
- Ask questions in issue discussions
- Check existing issues/PRs for similar work
- Review the documentation in `docs/`

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.

Thank you for contributing! 🎉
