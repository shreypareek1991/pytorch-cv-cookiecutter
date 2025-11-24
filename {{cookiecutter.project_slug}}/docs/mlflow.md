# MLflow Tracking

This project can provision a lightweight MLflow server via Docker Compose. The service name is `{{ cookiecutter.project_slug }}-mlflow`.

## Launch

```bash
cd mlflow
docker compose up -d
```

The server exposes:

- UI: http://localhost:5000
- Backend store: `{{ cookiecutter.mlflow_backend_store }}`
- Artifact root: `{{ cookiecutter.mlflow_artifact_root }}`

## Configure Training

Set the tracking URI inside `configs/tracking.yaml` or export:

```bash
export MLFLOW_TRACKING_URI=http://localhost:5000
export MLFLOW_EXPERIMENT_NAME={{ cookiecutter.project_name }}-experiments
```

`scripts/train.py` wires these env vars into MLflow callbacks.

## Tear Down

```
docker compose down
```

Backups live under `mlflow/storage/`.

