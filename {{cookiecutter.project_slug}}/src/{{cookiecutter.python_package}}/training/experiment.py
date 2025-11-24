"""Reusable training utilities for the project template."""

from __future__ import annotations

import pathlib
from dataclasses import dataclass
from typing import Iterable

import torch
from torch import nn, optim
from torch.utils.data import DataLoader
from torchvision import datasets, models, transforms


@dataclass
class ExperimentConfig:
    """Simplified subset of the Hydra-friendly training config."""

    data_root: pathlib.Path
    batch_size: int = 32
    num_workers: int = 4
    backbone: str = "resnet18"
    num_classes: int = 1000
    lr: float = 3e-4
    weight_decay: float = 0.05
    max_epochs: int = 5
    device: str = "{{ cookiecutter.default_device }}"


def create_transforms() -> transforms.Compose:
    return transforms.Compose(
        [
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225],
            ),
        ]
    )


def create_dataloader(cfg: ExperimentConfig, train: bool = True) -> DataLoader:
    dataset = datasets.ImageFolder(
        root=str(cfg.data_root / ("train" if train else "val")),
        transform=create_transforms(),
    )

    return DataLoader(
        dataset,
        batch_size=cfg.batch_size,
        shuffle=train,
        num_workers=cfg.num_workers,
        pin_memory=torch.cuda.is_available(),
    )


def create_model(cfg: ExperimentConfig) -> nn.Module:
    model_fn = getattr(models, cfg.backbone)
    model = model_fn(weights="DEFAULT")
    if hasattr(model, "fc") and isinstance(model.fc, nn.Linear):
        model.fc = nn.Linear(model.fc.in_features, cfg.num_classes)
    return model


def run_epoch(
    model: nn.Module,
    dataloader: DataLoader,
    criterion: nn.Module,
    optimizer: optim.Optimizer,
    device: torch.device,
    train: bool,
) -> float:
    model.train(train)
    running_loss = 0.0

    for batch in dataloader:
        inputs, targets = (tensor.to(device) for tensor in batch)

        with torch.set_grad_enabled(train):
            outputs = model(inputs)
            loss = criterion(outputs, targets)

            if train:
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

        running_loss += loss.detach().item()

    return running_loss / max(len(dataloader), 1)


def train(cfg: ExperimentConfig) -> Iterable[float]:
    device = torch.device(cfg.device if torch.cuda.is_available() else "cpu")
    model = create_model(cfg).to(device)
    optimizer = optim.AdamW(model.parameters(), lr=cfg.lr, weight_decay=cfg.weight_decay)
    criterion = nn.CrossEntropyLoss()

    train_loader = create_dataloader(cfg, train=True)
    val_loader = create_dataloader(cfg, train=False)

    for epoch in range(1, cfg.max_epochs + 1):
        train_loss = run_epoch(model, train_loader, criterion, optimizer, device, train=True)
        val_loss = run_epoch(model, val_loader, criterion, optimizer, device, train=False)
        yield epoch, train_loss, val_loss

    torch.save(model.state_dict(), cfg.data_root.parent / "artifacts" / "latest.pt")

