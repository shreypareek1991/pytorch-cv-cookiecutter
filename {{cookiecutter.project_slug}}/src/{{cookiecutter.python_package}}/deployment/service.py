"""FastAPI service shell for online inference."""

from __future__ import annotations

import pathlib
from functools import lru_cache
from typing import Annotated

import torch
from fastapi import FastAPI, File, UploadFile
from PIL import Image
from torchvision import transforms

app = FastAPI(title="{{ cookiecutter.project_name }} Inference")


@lru_cache
def _load_model(model_path: str) -> torch.nn.Module:
    model = torch.jit.load(model_path, map_location="cpu")
    model.eval()
    return model


PREPROC = transforms.Compose(
    [
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
    ]
)


@app.on_event("startup")
def startup_event() -> None:
    model_path = pathlib.Path("artifacts/latest.ts")
    if not model_path.exists():
        app.logger.warning("Model artifact %s was not found", model_path)
        return
    _load_model(str(model_path))


@app.post("/predict")
async def predict(file: Annotated[UploadFile, File(...)]) -> dict:
    image = Image.open(file.file).convert("RGB")
    tensor = PREPROC(image).unsqueeze(0)
    with torch.no_grad():
        outputs = _load_model("artifacts/latest.ts")(tensor)
        probs = torch.softmax(outputs, dim=1)
        confidence, pred = torch.max(probs, dim=1)

    return {
        "label": pred.item(),
        "confidence": confidence.item(),
    }

