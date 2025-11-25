# Troubleshooting

Common issues and their solutions.

## Installation Issues

### `uv sync` fails

**Error**: `uv sync failed: ...`

**Solutions**:
- Ensure Python {{ cookiecutter.python_version }} is installed: `python --version`
- Update `uv`: `pip install --upgrade uv` or follow [uv installation guide](https://docs.astral.sh/uv/)
- Check Python version compatibility with dependencies
- Try clearing cache: `uv cache clean`

### Command not found: `uv`

**Solution**: Install `uv`:
```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or via pip
pip install uv
```

See [uv installation guide](https://docs.astral.sh/uv/) for more options.

### Python version mismatch

**Error**: `Python version X.Y.Z is not supported`

**Solution**: 
- Install Python {{ cookiecutter.python_version }} or higher
- Use `pyenv` or `conda` to manage Python versions
- Verify: `uv run python --version`

## Docker Issues

### Docker build fails on ARM Mac

**Error**: `failed to solve: process did not complete successfully`

**Solutions**:
- Use CPU Dockerfile: `make docker-build-cpu`
- Or: `bash docker/build.sh --cpu`
- The build script automatically switches to CPU on ARM Macs

### CUDA not available

**Error**: `CUDA not available` or `NVIDIA driver not found`

**Solutions**:
- Use CPU Dockerfile: `make docker-build-cpu`
- For local development, use CPU device: `--device cpu`
- For CUDA support, ensure NVIDIA drivers and Container Toolkit are installed

### Docker image too large

**Solutions**:
- Use multi-stage builds (already implemented)
- Use `.dockerignore` to exclude unnecessary files
- Use CPU Dockerfile for smaller images: `make docker-build-cpu`

## Code Quality Issues

### Pre-commit hooks fail

**Error**: Hooks fail on commit

**Solutions**:
1. Auto-fix formatting: `make format`
2. Run hooks manually: `uv run pre-commit run --all-files`
3. Fix specific issues:
   - Formatting: `uv run black .`
   - Imports: `uv run isort .`
   - Linting: `uv run ruff check --fix .`

### MyPy type errors

**Error**: `error: Argument of type "X" cannot be assigned to parameter "Y"`

**Solutions**:
- Add type hints to your code
- Use `# type: ignore` for complex cases (sparingly)
- Check MyPy config in `pyproject.toml`
- Run: `uv run mypy src/ --ignore-missing-imports`

### Import errors

**Error**: `ModuleNotFoundError: No module named 'X'`

**Solutions**:
- Install missing dependency: `uv add package-name`
- Sync dependencies: `uv sync`
- Check if package is in correct extra: `uv sync --extra dev`

## Training Issues

### Out of memory (OOM)

**Error**: `RuntimeError: CUDA out of memory`

**Solutions**:
- Reduce batch size in config
- Use gradient accumulation
- Use CPU: `--device cpu` (slower but works)
- Use mixed precision training

### Model not training

**Checklist**:
- Verify data loading: Check data paths in config
- Check device: Ensure model and data are on same device
- Verify loss: Check if loss is decreasing
- Check learning rate: May be too high/low

### Slow training

**Solutions**:
- Use GPU if available: `--device cuda`
- Increase batch size (if memory allows)
- Use mixed precision training
- Profile code to find bottlenecks

## Git Issues

### Pre-commit hooks not running

**Solutions**:
- Install hooks: `make dev` or `uv run pre-commit install`
- Verify installation: `uv run pre-commit --version`
- Run manually: `uv run pre-commit run --all-files`

### Git remote not set

**Error**: `fatal: no upstream branch`

**Solutions**:
- Add remote: `git remote add origin <URL>`
- Set upstream: `git push -u origin main`
- See [Remote Repo Guide](remote_repo.md) for details

## MLflow Issues

{% if cookiecutter.enable_mlflow_tracking == "y" or cookiecutter.enable_mlflow_tracking == "yes" %}
### MLflow server not starting

**Error**: `Connection refused` or `Cannot connect to MLflow`

**Solutions**:
- Start MLflow server: `cd mlflow && docker-compose up -d`
- Check if port 5000 is available
- Verify tracking URI in `configs/tracking.yaml`
- Check Docker: `docker ps` to see if container is running

### Experiments not logging

**Solutions**:
- Verify MLflow server is running
- Check tracking URI configuration
- Ensure MLflow is installed: `uv sync --extra ml`
- Check logs for errors
{% else %}
MLflow is not enabled. See [Training Guide](TRAINING.md) to enable it.
{% endif %}

## Getting Help

1. **Check documentation**: Review relevant guides in `docs/`
2. **Check logs**: Look for error messages in terminal output
3. **Search issues**: Check if issue is already reported
4. **Review code**: Check code comments and docstrings

## Still Stuck?

- Review [Quick Reference](QUICK_REFERENCE.md) for common commands
- Check [Getting Started](GETTING_STARTED.md) for setup issues
- Review [Development Guide](DEVELOPMENT.md) for workflow questions

