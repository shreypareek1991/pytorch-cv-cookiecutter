# {{ cookiecutter.project_name }} API Application

This directory contains the FastAPI application for serving computer vision predictions via REST API.

## Overview

The application provides:
- **REST API** endpoints for image prediction
- **OpenAPI/Swagger documentation** at `/docs`
- **ReDoc documentation** at `/redoc`
- **Health check** endpoint at `/health`

## Quick Start

### Installing Dependencies

Before running the API, ensure all dependencies are installed:

```bash
# Install all dependencies including deploy extras (FastAPI, uvicorn, etc.)
uv sync --all-extras

# Or install just the deploy dependencies
uv sync --extra deploy

# If you need MLflow tracking
{% if cookiecutter.enable_mlflow_tracking == "y" or cookiecutter.enable_mlflow_tracking == "yes" %}
uv sync --extra ml
{% endif %}

# If you need DVC for data versioning
{% if cookiecutter.enable_dvc == "y" or cookiecutter.enable_dvc == "yes" %}
uv sync --extra dvc
{% endif %}
```

**Note**: The `deploy` extras include:
- `fastapi` - FastAPI framework
- `uvicorn[standard]` - ASGI server
- `python-multipart` - Required for file uploads

### Development Mode

```bash
# Run the development server
make app

# Or use uvicorn directly
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8080
```

The API will be available at:
- **API**: http://localhost:8080
- **Swagger UI**: http://localhost:8080/docs
- **ReDoc**: http://localhost:8080/redoc

### Production Mode

```bash
# Using uvicorn
uv run uvicorn app.main:app --host 0.0.0.0 --port 8080 --workers 4

# Or using Docker (see docker/ directory)
make docker build
make docker run
```

## API Endpoints

### `GET /`
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

### `GET /health`
Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "version": "0.1.0"
}
```

### `POST /predict`
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

### `POST /predict/url`
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

## Testing the API

### Using curl

```bash
# Health check
curl http://localhost:8080/health

# Predict from file
curl -X POST "http://localhost:8080/predict" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@path/to/image.jpg"

# Predict from URL
curl -X POST "http://localhost:8080/predict/url?image_url=https://example.com/image.jpg"
```

### Using Python requests

```python
import requests

# Health check
response = requests.get("http://localhost:8080/health")
print(response.json())

# Predict from file
with open("image.jpg", "rb") as f:
    files = {"file": f}
    response = requests.post("http://localhost:8080/predict", files=files)
    print(response.json())

# Predict from URL
response = requests.post(
    "http://localhost:8080/predict/url",
    params={"image_url": "https://example.com/image.jpg"}
)
print(response.json())
```

### Using Swagger UI

1. Start the server
2. Navigate to http://localhost:8080/docs
3. Click on an endpoint to expand it
4. Click "Try it out"
5. Fill in the parameters and click "Execute"

## Architecture

```
app/
├── main.py          # FastAPI application and routes
└── README.md        # This file

{{ cookiecutter.python_package }}/
├── vision.py        # Vision utilities and prediction logic
└── utils/           # Utility functions
```

The application uses code from the `{{ cookiecutter.python_package }}` package:
- `{{ cookiecutter.python_package }}.vision`: Image processing and prediction functions
- `{{ cookiecutter.python_package }}.utils`: Utility functions

## Customization

### Adding New Endpoints

1. Add route handlers in `app/main.py`:

```python
@app.get("/custom-endpoint")
async def custom_endpoint():
    return {"message": "Custom response"}
```

2. The endpoint will automatically appear in Swagger UI at `/docs`

### Updating Prediction Logic

Modify `{{ cookiecutter.python_package }}/vision.py`:
- Update `predict_simple()` function with your model
- Add new preprocessing/postprocessing functions
- Load your trained models from `science/models/`

### Environment Variables

You can configure the app using environment variables:

```bash
# .env file
API_HOST=0.0.0.0
API_PORT=8080
MODEL_PATH=science/models/best_model.pt
```

Then load them in `app/main.py`:

```python
import os
from dotenv import load_dotenv

load_dotenv()
host = os.getenv("API_HOST", "0.0.0.0")
port = int(os.getenv("API_PORT", 8080))
```

## Dependencies

### Required Dependencies

The API application requires the following dependencies (included in `deploy` extras):

- **fastapi** - Modern web framework for building APIs
- **uvicorn[standard]** - ASGI server implementation  
- **python-multipart** - Required for handling file uploads (multipart/form-data)

### Installing Dependencies

```bash
# Install all dependencies including deploy extras
uv sync --all-extras

# Or install just deploy dependencies
uv sync --extra deploy

# If you need MLflow tracking
{% if cookiecutter.enable_mlflow_tracking == "y" or cookiecutter.enable_mlflow_tracking == "yes" %}
uv sync --extra ml
{% endif %}

# If you need DVC for data versioning
{% if cookiecutter.enable_dvc == "y" or cookiecutter.enable_dvc == "yes" %}
uv sync --extra dvc
{% endif %}

# Verify installation
uv run python -c "import fastapi, uvicorn; print('Dependencies installed successfully')"
```

### Troubleshooting Dependency Issues

**Issue**: `ModuleNotFoundError: No module named 'uvicorn'`
- **Solution**: Run `uv sync --extra deploy` to install deploy dependencies

**Issue**: `RuntimeError: Form data requires "python-multipart" to be installed`
- **Solution**: `python-multipart` is included in deploy extras. Run `uv sync --extra deploy`

**Issue**: `ImportError: cannot import name 'app' from 'app.main'`
- **Solution**: Ensure you're in the project root directory and dependencies are synced

## Deployment

See `docs/docker.md` for Docker deployment instructions.

## Documentation

- **Swagger UI**: Interactive API documentation at `/docs`
- **ReDoc**: Alternative documentation at `/redoc`
- **OpenAPI Schema**: JSON schema at `/openapi.json`

