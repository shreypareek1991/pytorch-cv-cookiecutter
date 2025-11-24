from __future__ import annotations

import pathlib

import torch
import typer
import yaml

from {{ cookiecutter.python_package }}.training.experiment import create_model, ExperimentConfig

app = typer.Typer(help="Export the trained model to TorchScript or ONNX.")


@app.command()
def torchscript(
    config: pathlib.Path = pathlib.Path("configs/deployment.yaml"),
    output: pathlib.Path = pathlib.Path("artifacts/latest.ts"),
) -> None:
    cfg = yaml.safe_load(config.read_text())
    exp_cfg = ExperimentConfig(
        data_root=pathlib.Path("data"),  # not used for export
        batch_size=1,
        num_workers=0,
        backbone=cfg["export"].get("backbone", "resnet18"),
        num_classes=cfg["model"].get("num_classes", 1000) if "model" in cfg else 1000,
    )
    model = create_model(exp_cfg)
    checkpoint = pathlib.Path(cfg.get("model_path", "artifacts/latest.ckpt"))
    if checkpoint.exists():
        model.load_state_dict(torch.load(checkpoint, map_location="cpu"))
    scripted = torch.jit.script(model.eval())
    output.parent.mkdir(parents=True, exist_ok=True)
    scripted.save(str(output))
    typer.echo(f"Saved TorchScript artifact to {output}")


if __name__ == "__main__":
    app()

