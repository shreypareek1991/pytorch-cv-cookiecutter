import os
import platform
import shutil
import subprocess
from pathlib import Path


PROJECT_DIR = Path.cwd()
ENABLE_MLFLOW = "{{ cookiecutter.enable_mlflow_tracking }}".lower().startswith("y")
INSTALL_DEPS = "{{ cookiecutter.install_dependencies }}".lower().startswith("y")
USE_CUDA = "{{ cookiecutter.use_cuda_default }}".lower().startswith("y")


def remove_mlflow_assets() -> None:
    if ENABLE_MLFLOW:
        return
    shutil.rmtree(PROJECT_DIR / "mlflow", ignore_errors=True)
    mlflow_doc = PROJECT_DIR / "docs" / "mlflow.md"
    if mlflow_doc.exists():
        mlflow_doc.unlink()


def maybe_install_dependencies() -> None:
    if not INSTALL_DEPS:
        print("Skipping automatic uv install (per Cookiecutter prompt).")
        return

    try:
        subprocess.run(
            ["uv", "sync", "--all-extras"],
            check=True,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        print(f"⚠️  uv sync failed: {exc}. Install dependencies manually with `uv sync`.")


def init_git_repo() -> None:
    git_dir = PROJECT_DIR / ".git"
    if git_dir.exists():
        return
    try:
        subprocess.run(["git", "init"], check=True)
    except (OSError, subprocess.CalledProcessError):
        print("⚠️  Unable to run `git init`. Initialize git manually.")


def warn_on_cuda_on_arm() -> None:
    if not USE_CUDA:
        return
    if platform.machine().lower() == "arm64":
        print(
            "⚠️  CUDA base images rarely run natively on Apple Silicon. "
            "Use docker/Dockerfile.cpu or build with --platform=linux/amd64."
        )


def main() -> None:
    remove_mlflow_assets()
    init_git_repo()
    warn_on_cuda_on_arm()
    maybe_install_dependencies()
    print(
        "\nNext steps:\n"
        "  1. Review README.md for environment & Docker instructions.\n"
        "  2. Configure remotes via docs/remote_repo.md.\n"
        "  3. Update configs/training.yaml with your datasets.\n"
    )


if __name__ == "__main__":
    main()

