import os
import platform
import shutil
import subprocess
import sys
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


def show_configuration_summary() -> bool:
    """Display all selected settings and ask for confirmation."""
    print("\n" + "="*70)
    print("📋 PROJECT CONFIGURATION SUMMARY")
    print("="*70 + "\n")
    
    # Collect all settings
    settings = {
        "Project Information": {
            "Project Name": "{{ cookiecutter.project_name }}",
            "Project Slug": "{{ cookiecutter.project_slug }}",
            "Description": "{{ cookiecutter.project_description }}",
            "Python Package": "{{ cookiecutter.python_package }}",
        },
        "Author & Organization": {
            "Full Name": "{{ cookiecutter.full_name }}",
            "Organization": "{{ cookiecutter.organization }}",
            "Email": "{{ cookiecutter.email }}",
        },
        "Python & Runtime": {
            "Python Version": "{{ cookiecutter.python_version }}",
            "Default Device": "{{ cookiecutter.default_device }}",
        },
        "Docker Configuration": {
            "Docker Image": "{{ cookiecutter.docker_image_name }}",
            "Use CUDA": "{{ cookiecutter.use_cuda_default }}",
            "CUDA Version": "{{ cookiecutter.cuda_version }}",
            "Ubuntu Version": "{{ cookiecutter.base_ubuntu_version }}",
        },
        "MLflow Tracking": {
            "Enabled": "{{ cookiecutter.enable_mlflow_tracking }}",
        },
        "Setup Options": {
            "Auto-install Dependencies": "{{ cookiecutter.install_dependencies }}",
            "Repository Visibility": "{{ cookiecutter.repo_visibility }}",
        },
    }
    
    # Display settings with explanations
    explanations = {
        "Project Name": "Display name for your project",
        "Project Slug": "URL-friendly name (used in paths and imports)",
        "Description": "Brief description of your project",
        "Python Package": "Python package name (used in imports)",
        "Full Name": "Your name (appears in project metadata)",
        "Organization": "Your organization/company name",
        "Email": "Contact email for the project",
        "Python Version": "Python version to use (affects dependencies and Docker)",
        "Default Device": "Default compute device (cuda/cpu/mps)",
        "Docker Image": "Full Docker image name (registry/org/repo:tag)",
        "Use CUDA": "Whether to use CUDA-enabled Docker base image",
        "CUDA Version": "CUDA version for GPU support",
        "Ubuntu Version": "Ubuntu version for Docker base image",
        "Enabled": "Whether MLflow experiment tracking is enabled",
        "Backend Store": "MLflow backend database location",
        "Artifact Root": "MLflow artifact storage location",
        "Auto-install Dependencies": "Automatically run 'uv sync' after generation",
        "Repository Visibility": "Git repository visibility (private/public)",
    }
    
    for category, values in settings.items():
        print(f"📌 {category}:")
        for key, value in values.items():
            # Handle conditional values
            if key == "CUDA Version" and not USE_CUDA:
                value = "N/A (CPU only)"
            elif key == "Backend Store" and not ENABLE_MLFLOW:
                continue
            elif key == "Artifact Root" and not ENABLE_MLFLOW:
                continue
            
            explanation = explanations.get(key, "")
            print(f"   • {key:<25} : {value}")
            if explanation:
                print(f"     {' ' * 27} ({explanation})")
        
        # Add MLflow details if enabled
        if category == "MLflow Tracking" and ENABLE_MLFLOW:
            print(f"   • {'Backend Store':<25} : {{ cookiecutter.mlflow_backend_store }}")
            print(f"     {' ' * 27} (MLflow backend database location)")
            print(f"   • {'Artifact Root':<25} : {{ cookiecutter.mlflow_artifact_root }}")
            print(f"     {' ' * 27} (MLflow artifact storage location)")
        
        print()
    
    print("="*70)
    
    # Ask for confirmation
    while True:
        response = input("\n❓ Do you want to proceed with these settings? (yes/no): ").strip().lower()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            print("\n❌ Project generation cancelled. Please run cookiecutter again to change settings.")
            return False
        else:
            print("⚠️  Please enter 'yes' or 'no'.")


def main() -> None:
    # Show configuration summary and get confirmation
    if not show_configuration_summary():
        sys.exit(1)
    
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

