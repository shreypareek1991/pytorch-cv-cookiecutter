# API Reference

This page documents the API for {{ cookiecutter.project_name }}.

## Training API

### `scripts.train`

Main training script for model training.

```python
from scripts.train import app

# Run training
app.run()
```

**Command Line Usage:**

```bash
uv run python scripts/train.py run
uv run python scripts/train.py --config configs/training.yaml
```

**Options:**

- `--config`: Path to training configuration file
- `--device`: Device to use (cuda/cpu/mps)
- `--epochs`: Number of training epochs
- `--batch-size`: Batch size for training

## Export API

### `scripts.export`

Model export utilities for deployment.

```python
from scripts.export import app

# Export model
app.run()
```

**Command Line Usage:**

```bash
uv run python scripts/export.py \
    --checkpoint model.ckpt \
    --format onnx \
    --output model.onnx
```

**Options:**

- `--checkpoint`: Path to model checkpoint
- `--format`: Export format (onnx, torchscript)
- `--output`: Output file path
- `--input-shape`: Input tensor shape

## Serving API

### `scripts.serve`

FastAPI inference server.

```python
from scripts.serve import app

# Start server
app.run()
```

**Command Line Usage:**

```bash
uv run python scripts/serve.py --model model.pt
uv run python scripts/serve.py --model model.pt --port 8000
```

**REST API Endpoints:**

- `POST /predict` - Run inference
  - Request body: JSON with input data
  - Response: JSON with predictions

- `GET /health` - Health check
  - Response: `{"status": "healthy"}`

- `GET /docs` - API documentation (Swagger UI)

## Source Code API

### Data Module

```python
from {{ cookiecutter.python_package }}.data import DataModule

# Create data module
data_module = DataModule(config)
```

### Training Module

```python
from {{ cookiecutter.python_package }}.training import Trainer

# Create trainer
trainer = Trainer(config)
```

### Deployment Module

```python
from {{ cookiecutter.python_package }}.deployment import ModelServer

# Create model server
server = ModelServer(model_path)
```

## Configuration

All APIs use configuration files in `configs/`:

- `configs/training.yaml` - Training configuration
- `configs/model.yaml` - Model configuration
- `configs/deployment.yaml` - Deployment configuration

See individual configuration files for detailed options.

