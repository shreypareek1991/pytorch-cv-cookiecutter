"""Main FastAPI application with OpenAPI/Swagger documentation."""

from __future__ import annotations

import pathlib
from typing import Any

import uvicorn
from fastapi import FastAPI, File, HTTPException, UploadFile
from pydantic import BaseModel

from {{ cookiecutter.python_package }} import __version__
from {{ cookiecutter.python_package }}.vision import predict_simple

# Create FastAPI app with OpenAPI documentation
app = FastAPI(
    title="{{ cookiecutter.project_name }} API",
    description="{{ cookiecutter.project_description }}",
    version=__version__,
    docs_url="/docs",  # Swagger UI
    redoc_url="/redoc",  # ReDoc alternative
    openapi_url="/openapi.json",  # OpenAPI schema
)


# Response models
class HealthResponse(BaseModel):
    """Health check response model."""

    status: str
    version: str


class PredictionResponse(BaseModel):
    """Prediction response model."""

    prediction: dict[str, Any]
    message: str


# API Routes
@app.get("/", response_model=dict[str, str])
async def root() -> dict[str, str]:
    """Root endpoint with API information."""
    return {
        "name": "{{ cookiecutter.project_name }}",
        "description": "{{ cookiecutter.project_description }}",
        "version": __version__,
        "docs": "/docs",
        "redoc": "/redoc",
    }


@app.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    """Health check endpoint."""
    return HealthResponse(status="healthy", version=__version__)


@app.post("/predict", response_model=PredictionResponse)
async def predict(file: UploadFile = File(...)) -> PredictionResponse:  # noqa: B008
    """Predict endpoint for image classification.

    Upload an image file and get predictions.

    Args:
        file: Image file to process (JPEG, PNG, etc.)

    Returns:
        Prediction results with confidence scores.

    Raises:
        HTTPException: If file is invalid or processing fails.
    """
    # Validate file type
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")

    try:
        # Save uploaded file temporarily
        temp_path = pathlib.Path(f"/tmp/{file.filename}")
        with temp_path.open("wb") as f:
            content = await file.read()
            f.write(content)

        # Run prediction
        prediction = predict_simple(temp_path)

        # Clean up temp file
        temp_path.unlink()

        return PredictionResponse(
            prediction=prediction,
            message="Prediction completed successfully",
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}") from e


@app.post("/predict/url", response_model=PredictionResponse)
async def predict_from_url(image_url: str) -> PredictionResponse:
    """Predict from image URL.

    Args:
        image_url: URL of the image to process.

    Returns:
        Prediction results.

    Raises:
        HTTPException: If URL is invalid or processing fails.
    """
    try:
        from urllib import request

        # Download image
        temp_path = pathlib.Path("/tmp/downloaded_image.jpg")
        request.urlretrieve(image_url, temp_path)

        # Run prediction
        prediction = predict_simple(temp_path)

        # Clean up temp file
        temp_path.unlink()

        return PredictionResponse(
            prediction=prediction,
            message="Prediction completed successfully",
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}") from e


def run_server(host: str = "0.0.0.0", port: int = 8080, reload: bool = False) -> None:
    """Run the FastAPI server.

    Args:
        host: Host to bind to.
        port: Port to bind to.
        reload: Enable auto-reload for development.
    """
    uvicorn.run(app, host=host, port=port, reload=reload)


if __name__ == "__main__":
    run_server(reload=True)

