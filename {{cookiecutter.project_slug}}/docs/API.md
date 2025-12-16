# API Reference

This document provides API reference for the {{ cookiecutter.project_name }} project.

## FastAPI Application

The main API application is located in `app/main.py` and provides REST endpoints for computer vision tasks.

### Running the API

```bash
# Development mode
make app

# Or using uvicorn directly
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8080

# Production mode
uv run uvicorn app.main:app --host 0.0.0.0 --port 8080 --workers 4
```

### API Endpoints

#### `GET /`
Root endpoint with API information.

**Response:**
```json
{
  "name": "{{ cookiecutter.project_name }}",
  "description": "{{ cookiecutter.project_description }}",
  "version": "0.1.0",
  "docs": "/docs",
  "redoc": "/redoc"
}
```

#### `GET /health`
Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "version": "0.1.0"
}
```

#### `POST /predict`
Upload an image file and get predictions.

**Request:**
- Content-Type: `multipart/form-data`
- Body: Image file (JPEG, PNG, etc.)

**Response:**
```json
{
  "prediction": {
    "image_shape": [224, 224, 3],
    "processed_shape": [1, 3, 224, 224],
    "prediction": "placeholder",
    "confidence": 0.0
  },
  "message": "Prediction completed successfully"
}
```

#### `POST /predict/url`
Predict from an image URL.

**Request:**
- Content-Type: `application/json`
- Body:
```json
{
  "image_url": "https://example.com/image.jpg"
}
```

**Response:**
Same as `/predict` endpoint.

### OpenAPI Documentation

The API includes automatic OpenAPI/Swagger documentation:

- **Swagger UI**: http://localhost:8080/docs
- **ReDoc**: http://localhost:8080/redoc
- **OpenAPI Schema**: http://localhost:8080/openapi.json

## Python Package API

### Vision Module

The `{{ cookiecutter.python_package }}.vision` module provides computer vision utilities.

#### `load_image(image_path: str | pathlib.Path) -> np.ndarray`

Load an image from file path.

**Parameters:**
- `image_path`: Path to the image file

**Returns:**
- Image as numpy array in RGB format

**Example:**
```python
from {{ cookiecutter.python_package }}.vision import load_image

image = load_image("path/to/image.jpg")
```

#### `preprocess_image(image: np.ndarray, size: tuple[int, int] = (224, 224)) -> torch.Tensor`

Preprocess image for model inference.

**Parameters:**
- `image`: Image as numpy array (H, W, C) in RGB format
- `size`: Target size (height, width), default (224, 224)

**Returns:**
- Preprocessed image as torch tensor (1, C, H, W) normalized to [0, 1]

**Example:**
```python
from {{ cookiecutter.python_package }}.vision import preprocess_image

tensor = preprocess_image(image, size=(224, 224))
```

#### `predict_simple(image_path: str | pathlib.Path) -> dict[str, Any]`

Simple example prediction function.

**Parameters:**
- `image_path`: Path to the image file

**Returns:**
- Dictionary with prediction results

**Example:**
```python
from {{ cookiecutter.python_package }}.vision import predict_simple

result = predict_simple("path/to/image.jpg")
```

### Utils Module

The `{{ cookiecutter.python_package }}.utils` module provides utility functions.

#### `save_state(state: Mapping[str, Any], directory: pathlib.Path, prefix: str = "checkpoint") -> pathlib.Path`

Save a state dictionary to a checkpoint file.

**Parameters:**
- `state`: State dictionary to save
- `directory`: Directory to save checkpoint in
- `prefix`: Filename prefix, default "checkpoint"

**Returns:**
- Path to saved checkpoint file

**Example:**
```python
from {{ cookiecutter.python_package }}.utils import save_state
import pathlib

checkpoint_path = save_state(
    {"model": model.state_dict(), "epoch": 10},
    pathlib.Path("science/models"),
    prefix="model"
)
```

#### `load_state(path: pathlib.Path) -> Mapping[str, Any]`

Load a state dictionary from a checkpoint file.

**Parameters:**
- `path`: Path to checkpoint file

**Returns:**
- State dictionary

**Raises:**
- `FileNotFoundError`: If checkpoint file doesn't exist

**Example:**
```python
from {{ cookiecutter.python_package }}.utils import load_state
import pathlib

state = load_state(pathlib.Path("science/models/model-checkpoint-20240101-120000.pt"))
```

## Configuration

API configuration is managed through:

- `configs/deployment.yaml` - Server configuration (host, port, workers, etc.)
- Environment variables - Can override config values

## See Also

- [API Application Guide](../app/README.md) - Detailed guide for using the FastAPI application
- [Getting Started](GETTING_STARTED.md) - Setup and installation
- [Development Guide](DEVELOPMENT.md) - Development workflow
