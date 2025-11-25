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
        return
    
    # Install pre-commit hooks if dependencies were installed successfully
    install_pre_commit_hooks()


def install_pre_commit_hooks() -> None:
    """Install pre-commit hooks if pre-commit is available."""
    try:
        subprocess.run(
            ["uv", "run", "pre-commit", "install"],
            check=True,
            cwd=PROJECT_DIR,
        )
        print("✅ Pre-commit hooks installed successfully!")
    except (OSError, subprocess.CalledProcessError):
        print("⚠️  Pre-commit hooks not installed. Run 'make dev' or 'uv run pre-commit install' manually.")


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
    project_slug = "{{ cookiecutter.project_slug }}"
    
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

    🔧 Getting Started:
      
      1. Navigate to your project:
         cd {project_slug}
      
      2. Activate the virtual environment:
         source .venv/bin/activate
         
         Or use uv (no activation needed):
         uv run python scripts/train.py
      
      3. Useful commands to try:
         • make sync              - Sync all dependencies
         • make dev               - Install pre-commit hooks
         • make test              - Run tests
         • make format            - Format code (black, isort, ruff)
         • make lint              - Lint code (ruff, mypy)
         • make pre-commit        - Run all pre-commit checks
         • make docker-build      - Build Docker image
         • make docker-build-scan - Build and scan Docker image
         • uv run train_model --help    - See training options
         • uv run pytest          - Run tests
         • uv run python scripts/train.py run  - Start training

    📚 Documentation:
      • README.md - Project overview and setup
      • docs/docker.md - Docker usage and scanning
      • docs/mlflow.md - MLflow tracking setup
      • docs/remote_repo.md - Git remote configuration

    💡 Next Steps:
      1. Review README.md for detailed documentation
      2. Configure your datasets in configs/training.yaml
      3. Set up remote repository (see docs/remote_repo.md)
      4. Run tests: make test or uv run pytest
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
    
    # Remind about pre-commit if dependencies weren't auto-installed
    if not INSTALL_DEPS:
        print("\n💡 Tip: Install pre-commit hooks with 'make dev' or 'uv run pre-commit install'")


if __name__ == "__main__":
    main()

