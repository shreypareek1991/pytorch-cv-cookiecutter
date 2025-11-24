from __future__ import annotations

import pathlib

import typer
import yaml

from {{ cookiecutter.python_package }}.training.experiment import ExperimentConfig, train

app = typer.Typer(help="Model training entrypoint.")


@app.command()
def run(config: pathlib.Path = pathlib.Path("configs/training.yaml")) -> None:
    """Train the model using a YAML config."""
    cfg_dict = yaml.safe_load(config.read_text())
    exp_cfg = ExperimentConfig(
        data_root=pathlib.Path(cfg_dict["train_data"]["root"]).resolve(),
        batch_size=cfg_dict["train_data"]["batch_size"],
        num_workers=cfg_dict["train_data"]["num_workers"],
        backbone=cfg_dict["model"]["backbone"],
        num_classes=cfg_dict["model"]["num_classes"],
        lr=cfg_dict["optimizer"]["lr"],
        weight_decay=cfg_dict["optimizer"]["weight_decay"],
        max_epochs=cfg_dict["max_epochs"],
        device=cfg_dict.get("device", "{{ cookiecutter.default_device }}"),
    )

    for epoch, train_loss, val_loss in train(exp_cfg):
        typer.echo(f"epoch={epoch} train_loss={train_loss:.4f} val_loss={val_loss:.4f}")


if __name__ == "__main__":
    app()

