# Contributing to PyTorch CV Cookiecutter Template

Thank you for your interest in contributing! This guide will help you get started with contributing to this template repository.

## Getting Started

### Prerequisites

- Python ≥ 3.11
- `git` installed
- `cookiecutter` installed (`uv tool install cookiecutter` or `pipx install cookiecutter`)
- `uv` CLI installed (https://docs.astral.sh/uv/)

### Cloning the Repository

```bash
# Clone the repository
git clone https://github.com/shreypareek1991/pytorch-cv-cookiecutter.git
cd pytorch-cv-cookiecutter

# Or if you've already cloned it, update to latest
git pull origin main
```

### Setting Up Your Development Environment

1. **Install dependencies** (if any):
   ```bash
   # This template doesn't require dependencies for development,
   # but if you need to test with cookiecutter:
   uv tool install cookiecutter
   ```

2. **Test the template locally**:
   ```bash
   # Test rendering with default values
   cookiecutter . --no-input
   
   # Or test with custom values
   cookiecutter . --no-input project_name="Test Project" python_version="3.12"
   ```

3. **Verify generated project**:
   ```bash
   cd test-project  # or your test project name
   uv sync --extra dev
   make test
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
   - Edit template files in `{{cookiecutter.project_slug}}/`
   - Update hooks in `hooks/`
   - Modify `cookiecutter.json` for new prompts
   - Update documentation as needed

3. **Test your changes**:
   ```bash
   # Render the template with your changes
   cookiecutter . --no-input
   
   # Navigate to generated project
   cd <generated-project-name>
   
   # Verify it works
   uv sync --extra dev
   make test
   make format
   make lint
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

- ✅ Template renders without errors
- ✅ Generated project structure is correct
- ✅ All hooks execute successfully
- ✅ Generated project can install dependencies (`uv sync`)
- ✅ Generated project tests pass (`make test`)
- ✅ Generated project can build Docker images (if applicable)
- ✅ Documentation is updated if needed

### Running Tests on Generated Project

```bash
# After generating a test project
cd <generated-project-name>

# Install dependencies
uv sync --extra dev

# Run tests
make test

# Check formatting
make format

# Run linting
make lint

# Test Docker build (if applicable)
make docker-build
```

## Submitting a Pull Request

### Before Submitting

1. **Update documentation** if your changes affect:
   - Template prompts or defaults
   - Project structure
   - Dependencies or requirements
   - Hooks behavior

2. **Test thoroughly**:
   - Generate a fresh project with your changes
   - Verify all features work as expected
   - Check that existing functionality isn't broken

3. **Keep PRs focused**:
   - One feature or fix per PR
   - Keep changes small and reviewable
   - Include clear description of what changed and why

### PR Process

1. **Push your branch**:
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create a Pull Request** on GitHub:
   - Provide a clear title and description
   - Reference any related issues
   - Include screenshots or examples if applicable
   - List what you tested

3. **Respond to feedback**:
   - Address review comments promptly
   - Make requested changes
   - Update your branch as needed

### PR Checklist

- [ ] Changes tested locally
- [ ] Generated project works correctly
- [ ] Documentation updated (if needed)
- [ ] Commit messages follow conventions
- [ ] No breaking changes (or clearly documented)
- [ ] All tests pass in generated project

## Code Style

- Follow Python PEP 8 style guidelines
- Use meaningful variable and function names
- Add comments for complex logic
- Keep template files clean and well-organized
- Use consistent indentation (spaces, not tabs)

## Project Structure

Understanding the template structure:

```
.
├── cookiecutter.json          # Template variables and prompts
├── hooks/
│   ├── pre_gen_project.py     # Pre-generation hook (runs before template rendering)
│   └── post_gen_project.py    # Post-generation hook (runs after template rendering)
├── {{cookiecutter.project_slug}}/  # Template files (will be rendered)
│   ├── src/                   # Source code structure
│   ├── scripts/               # Entrypoint scripts
│   ├── configs/               # Configuration files
│   ├── docker/                # Docker files
│   ├── tests/                 # Test files
│   └── ...                    # Other template files
├── README.md                  # Template repository README
└── CONTRIBUTING.md            # This file
```

## Common Contribution Areas

### Adding New Template Variables

1. Add variable to `cookiecutter.json`:
   ```json
   {
     "new_variable": "default_value",
     ...
   }
   ```

2. Use in template files: `{{ cookiecutter.new_variable }}`

3. Update documentation if it affects user experience

### Modifying Hooks

- `pre_gen_project.py`: Runs before template rendering
  - Use for validation, displaying messages, etc.
  - Cannot modify template variables

- `post_gen_project.py`: Runs after template rendering
  - Use for git init, dependency installation, cleanup, etc.
  - Can modify generated files

### Adding Dependencies

Update `{{cookiecutter.project_slug}}/pyproject.toml`:
- Add to `[project.dependencies]` for runtime deps
- Add to `[project.optional-dependencies.dev]` for dev tools
- Add to `[project.optional-dependencies.deploy]` for deployment

### Adding New Scripts

Add to `{{cookiecutter.project_slug}}/scripts/` and reference in:
- `README.md` (project documentation)
- `Makefile` (if it should be a make target)

## Questions?

- Open an issue for bugs or feature requests
- Ask questions in issue discussions
- Check existing issues/PRs for similar work

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.

Thank you for contributing! 🎉

