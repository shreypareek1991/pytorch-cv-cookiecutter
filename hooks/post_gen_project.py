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
            ["uv", "sync", "--extra", "dev"],
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


def print_success_message() -> None:
    """Display success message after project generation."""
    project_name = "{{ cookiecutter.project_name }}"
    
    success = f"""
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║              ✅ Project Generated Successfully!           ║
    ║                                                           ║
    ║              Project: {project_name:<30} ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝

    🎉 Congratulations! Your PyTorch Computer Vision project is ready.

    📁 Project Structure:
      • Source code: src/{{ cookiecutter.python_package }}/
      • Training scripts: scripts/train.py
      • Deployment: scripts/serve.py
      • Configuration: configs/
      • Docker files: docker/
      • Tests: tests/

    🚀 Quick Start:
      1. Review README.md for detailed documentation
      2. Configure your datasets in configs/training.yaml
      3. Set up remote repository (see docs/remote_repo.md)
      4. Start training: uv run train_model --help

    📚 Documentation:
      • Docker setup: docs/docker.md
      • MLflow tracking: docs/mlflow.md
      • Remote repo: docs/remote_repo.md

    💡 Next Steps:
      1. Review README.md for environment & Docker instructions
      2. Configure remotes via docs/remote_repo.md
      3. Update configs/training.yaml with your datasets
      4. Run tests: uv run pytest
      5. Start developing! 🚀

    Happy coding! 🎊
    """
    print(success)


def main() -> None:
    print("\n🔧 Setting up your project...\n")
    
    print("📦 Removing MLflow assets (if disabled)...")
    remove_mlflow_assets()
    
    print("📂 Initializing Git repository...")
    init_git_repo()
    
    warn_on_cuda_on_arm()
    
    print("📥 Installing dependencies...")
    maybe_install_dependencies()
    
    print("\n✨ Finalizing setup...\n")
    print_success_message()


if __name__ == "__main__":
    main()

