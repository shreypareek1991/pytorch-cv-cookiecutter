# Training & Deployment Guide

This guide covers model training, export, and serving.

## Training

### Basic Training

Train your models using the provided training script:

```bash
# Basic training with default config
uv run python scripts/train.py

# With custom config file
uv run python scripts/train.py --config configs/training.yaml

# See all available options
uv run python scripts/train.py --help
```

### Training Scripts

- **`scripts/train.py`**: Main training loop with configurable trainer/device
- **`scripts/export.py`**: Export models for deployment (TorchScript/ONNX)
- **`scripts/serve.py`**: FastAPI microservice for inference

### Configuration

Training configuration is managed through YAML files:

- **Training configs**: `configs/training.yaml` - Training hyperparameters, epochs, batch size
- **Model configs**: `configs/model.yaml` - Model architecture and parameters
- **Deployment configs**: `configs/deployment.yaml` - Serving and export settings
- **Environment variables**: `.env` - Secrets and API keys (see `.env.example`)

### Device Selection

The default device is `{{ cookiecutter.default_device }}`. You can override it:

```bash
# Use CPU
uv run python scripts/train.py --device cpu

# Use CUDA (if available)
uv run python scripts/train.py --device cuda

# Use MPS (Apple Silicon)
uv run python scripts/train.py --device mps
```

## Model Export

Export trained models for deployment in various formats:

### Export Formats

```bash
# Export to ONNX
uv run python scripts/export.py \
    --checkpoint path/to/checkpoint.ckpt \
    --format onnx \
    --output model.onnx

# Export to TorchScript
uv run python scripts/export.py \
    --checkpoint path/to/checkpoint.ckpt \
    --format torchscript \
    --output model.pt
```

### Export Options

```bash
# See all export options
uv run python scripts/export.py --help

# Common options:
# --checkpoint: Path to model checkpoint
# --format: Export format (onnx, torchscript)
# --output: Output file path
# --input-shape: Input tensor shape
```

## Serving

### FastAPI Inference Server

Start a FastAPI microservice for model inference:

```bash
# Start server with default model
uv run python scripts/serve.py --model path/to/model.pt

# Specify port
uv run python scripts/serve.py --model path/to/model.pt --port 8000

# With custom config
uv run python scripts/serve.py \
    --model path/to/model.pt \
    --config configs/deployment.yaml
```

### API Endpoints

The server provides REST API endpoints:

- `POST /predict` - Run inference
- `GET /health` - Health check
- `GET /docs` - API documentation (Swagger UI)

### Docker Deployment

Deploy the model using Docker:

```bash
# Build Docker image
make docker-build

# Run container
make docker-run

# Or manually
docker run -p 8000:8000 \
    -v $(pwd)/models:/app/models \
    {{ cookiecutter.docker_image_name }}
```

See [Docker Guide](docker.md) for detailed Docker instructions.

## Experiment Tracking

{% if cookiecutter.enable_mlflow_tracking == "y" or cookiecutter.enable_mlflow_tracking == "yes" %}
This project uses **MLflow** for experiment tracking.

### Starting MLflow Server

```bash
# Using Docker Compose (recommended)
cd mlflow
docker-compose up -d

# Access UI at http://localhost:5000
```

### Configuration

- **Backend store**: `{{ cookiecutter.mlflow_backend_store }}`
- **Artifact root**: `{{ cookiecutter.mlflow_artifact_root }}`
- **Tracking URI**: Configured in `configs/tracking.yaml`

### Usage

The training script automatically logs to MLflow:

- Metrics (loss, accuracy, etc.)
- Parameters (hyperparameters, configs)
- Artifacts (models, plots, etc.)

View experiments at:
- Local: http://localhost:5000
- Remote: Configure in `configs/tracking.yaml`

See [MLflow Guide](mlflow.md) for detailed setup and usage.
{% else %}
MLflow tracking is not enabled for this project. To enable it:

1. Set up MLflow server
2. Configure tracking URI in `configs/tracking.yaml`
3. Update training scripts to log metrics
{% endif %}

## Best Practices

### Training

1. **Use configs**: Keep hyperparameters in YAML configs, not code
2. **Version control**: Commit configs to track experiment configurations
3. **Checkpoints**: Save model checkpoints regularly
4. **Logging**: Use MLflow or similar for experiment tracking
5. **Validation**: Always validate on a held-out test set

### Deployment

1. **Export formats**: Prefer ONNX for cross-platform deployment
2. **Input validation**: Validate inputs in serving endpoints
3. **Error handling**: Handle edge cases gracefully
4. **Monitoring**: Monitor model performance in production
5. **Versioning**: Version your models and track deployments

## Next Steps

- Review [Docker Guide](docker.md) for containerized deployment
- Check [Quick Reference](QUICK_REFERENCE.md) for common commands
- See [Troubleshooting](TROUBLESHOOTING.md) for common issues

