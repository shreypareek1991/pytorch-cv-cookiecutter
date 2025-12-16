"""Helpers for saving / loading checkpoints consistently."""

from __future__ import annotations

import datetime as dt
import pathlib
from typing import Any, Mapping

import torch


def save_state(
    state: Mapping[str, Any],
    directory: pathlib.Path,
    prefix: str = "checkpoint",
) -> pathlib.Path:
    """Save state dictionary to checkpoint file.

    Args:
        state: State dictionary to save.
        directory: Directory to save checkpoint in.
        prefix: Filename prefix for checkpoint.

    Returns:
        Path to saved checkpoint file.
    """
    directory.mkdir(parents=True, exist_ok=True)
    timestamp = dt.datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    path = directory / f"{prefix}-{timestamp}.pt"
    torch.save(state, path)
    return path


def load_state(path: pathlib.Path) -> Mapping[str, Any]:
    """Load state dictionary from checkpoint file.

    Args:
        path: Path to checkpoint file.

    Returns:
        Loaded state dictionary.

    Raises:
        FileNotFoundError: If checkpoint file does not exist.
    """
    if not path.exists():
        raise FileNotFoundError(f"Checkpoint {path} does not exist")
    return torch.load(path, map_location="cpu")

