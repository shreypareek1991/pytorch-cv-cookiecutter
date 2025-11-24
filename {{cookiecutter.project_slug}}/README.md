# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

This template ships with sensible defaults for computer-vision work using PyTorch, `uv` for packaging, Docker images for both CUDA and CPU targets, and optional MLflow tracking. Answer the Cookiecutter prompts to describe your project (name, org, author, Docker image, Python version, CUDA preference, MLflow usage, and whether `uv` should auto-install dependencies).

## Project Structure

```
.
├── configs/                # Hydra/YAML configs for training & deployment
├── docker/                 # Dockerfiles, build & run scripts, OS package lists
├── docs/                   # How-to guides (remote repo, MLflow, Docker)
├── scripts/                # Entrypoints for training/inference/utilities
├── src/{{ cookiecutter.python_package }}/
│   ├── data/               # Dataset + datamodule helpers
│   ├── training/           # Lightning/Trainer orchestration
│   ├── deployment/         # Serving utilities / export logic
│   └── utils/              # Shared helpers (metrics, transforms, etc.)
└── tests/                  # Pytest-based smoke & regression tests
```

## Environment Management (uv)

- Sync dependencies: `uv sync`
- Run scripts: `uv run python scripts/train.py`
- Add dev tools: `uv add --group dev ruff`
- Export lockfile for CI/CD: `uv lock`

If you opted into automatic installation, `uv sync --all-extras` ran right after project creation. Otherwise, start with `uv sync` (or `uv sync --group dev` to include development tooling).

## Training & Deployment

- `scripts/train.py`: reference training loop with configurable trainer/device.
- `scripts/export.py`: package weights for deployment (TorchScript/ONNX hooks).
- `scripts/serve.py`: FastAPI microservice template for inference.
- Configuration lives inside `configs/` and uses environment overrides.

## Docker Workflow

Dockerfiles live in `docker/`:

- `Dockerfile` targets CUDA by default (image `nvidia/cuda:{{ cookiecutter.cuda_version }}-cudnn9-runtime-ubuntu{{ cookiecutter.base_ubuntu_version }}`) but gracefully downgrades to a slim CPU base on Apple Silicon or when CUDA is disabled during Cookiecutter prompts.
- `Dockerfile.cpu` is always CPU-only and better suited for ARM Macs.
- `apt-packages.txt` lists OS-level dependencies installed via `apt-get`.
- `build.sh` and `run.sh` wrap `docker build`/`docker run` with arch detection and multi-platform hints; read them before running on ARM Macs.

## Experiment Tracking (optional)

If you enabled MLflow:

- `mlflow/docker-compose.yml` spins up a server named `{{ cookiecutter.project_slug }}-mlflow`.
- `docs/mlflow.md` documents how to launch the server locally or in Docker, wiring the backend store (`{{ cookiecutter.mlflow_backend_store }}`) and artifact root (`{{ cookiecutter.mlflow_artifact_root }}`).
- The training script logs metrics/artifacts to the MLflow URI in `configs/tracking.yaml`.

Otherwise those files are omitted automatically.

## Remote Repository Instructions

After rendering the template and initializing git (`git init` is already done for you by Cookiecutter), wire it to a remote:

1. Create an empty repository (e.g. GitHub/GitLab) and copy the URL (SSH or HTTPS).
2. Add the remote: `git remote add origin <REMOTE_URL>`.
3. Push the main branch: `git push -u origin main`.
4. Configure protected branches, CI secrets, and deploy keys as needed.

See `docs/remote_repo.md` for more detail, including PAT-based pushes and multi-remote setups.

## Next Steps

1. Create a `.env` (see `.env.example`) and set secrets such as MLflow credentials.
2. Run `uv run pytest` to verify the environment & tests.
3. Update `configs/*.yaml` to match your data sources and deployment targets.
4. If deploying with CUDA, install the latest NVIDIA Container Toolkit before building images.

Happy building! 🚀

