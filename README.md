# PyTorch CV Cookiecutter Template

This repository bootstraps computer-vision projects that use PyTorch, uv-based dependency management, Dockerized CUDA/CPU images, and optional MLflow tracking.

## Usage

### 🎯 Recommended: Use the installer (shows logo & welcome message first)

**One-liner installation:**
```bash
curl -fsSL https://raw.githubusercontent.com/shreypareek1991/pytorch-cv-cookiecutter/main/install.sh | bash
```

**Or clone and run the wrapper:**
```bash
# Clone this repository
git clone https://github.com/shreypareek1991/pytorch-cv-cookiecutter.git
cd pytorch-cv-cookiecutter

# Run the wrapper script
./run_template.sh
```

The installer/wrapper will:
1. ✅ Display your company logo
2. ✅ Show a welcome message with descriptions of all questions
3. ✅ Wait for you to press Enter
4. ✅ Then start the cookiecutter prompts

### Standard cookiecutter command (no welcome message)

```bash
# Direct usage (prompts appear immediately, no logo/welcome)
cookiecutter https://github.com/shreypareek1991/pytorch-cv-cookiecutter

# Or locally once cloned:
cookiecutter /path/to/this/repo
```

**Note:** When using the direct `cookiecutter` command, the logo and welcome message will appear AFTER you answer all prompts (due to cookiecutter's execution order).

### Prompts

You will be asked for:

- Author info (`full_name`, `organization`, `email`)
- Project metadata (`project_name`, `project_description`, `project_slug`, `python_package`)
- Tooling choices (`python_version`, `install_dependencies`, `repo_visibility`)
- Deployment knobs (`docker_image_name`, `use_cuda_default`, `cuda_version`, `base_ubuntu_version`)
- Experiment tracking (`enable_mlflow_tracking`, `mlflow_*`)

Defaults are safe; anything that can be derived (e.g., `project_slug`) is pre-populated automatically.

## What You Get

- uv-managed project with dev/deploy extras and scripts for training/export/serving.
- Dockerfiles + helper scripts for CUDA (amd64) and CPU (arm64-friendly) targets, including OS package manifests.
- Optional MLflow server scaffolding (removed if tracking is disabled).
- Post-gen hook that can auto-run `uv sync`, initialize git, and warn if CUDA is selected on Apple Silicon.
- Documentation covering Docker, MLflow, and how to connect to a remote git repository.

## Requirements

- Python ≥ 3.11
- `cookiecutter` (install via `uv tool install cookiecutter` or `pipx install cookiecutter`)
- `uv` CLI (https://docs.astral.sh/uv/)

## Development

1. Render locally for testing: `cookiecutter . --no-input project_name=TestProject ...`
2. Validate hook behaviour by checking the rendered directory.
3. Publish to GitHub/GitLab and tag releases for discoverability.

