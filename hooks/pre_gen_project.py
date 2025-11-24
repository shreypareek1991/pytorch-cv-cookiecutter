#!/usr/bin/env python3
"""
Pre-generation hook for cookiecutter template.
Displays welcome message and company logo before prompting user.
"""

import sys
from pathlib import Path


def print_logo() -> None:
    """Display company logo as ASCII art."""
    # Try to load logo from file, fallback to default
    hook_dir = Path(__file__).parent
    logo_file = hook_dir / "logo.txt"
    
    if logo_file.exists():
        try:
            logo = logo_file.read_text()
            print(logo)
            return
        except Exception:
            pass
    
    # Default logo if file doesn't exist
    logo = """
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║                                                           ║
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@
    @@@*     @. .   % .@@@  @       @@  @@   @@@@@@@@@@@
    @@@@@  @@@.  *@@% .@@@  @  *@@  :@  #  +@@@@@@@@@@@@
    @@@@@ #@@@. .@@@@ .@@@  @  @@@- .@     @@@@@@@@@@@@@
    @@@@@  @@@. .@@@@ .@@@  @  @@@- .@  %.  @@@@@@@@@@@@
    @@@@@. .%.. .@@@@       @  @@@- .@  @@-  @  *@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@  :@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@
    @@@@@@@@@     .@#     .@@:     -@@  @@      @@@@@@@@
    @@@@@@@@@@  :@@@  @@@= .: .@@@  :@  @. #@@+ .@@@@@@@
    @@@@@@@@@@  :@@@  @@@+  . .@@@  :@  @%      #@@@@@@@
    @@@@@@@@@@  :@@@  @@@+  . .@@@  :%  @##@@@@  @@@@@@@
    @@@@@@@@@@*    @       @@       @@   % - @  #@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
║              Computer Vision Template                     ║
║              Powered by PyTorch & UV                      ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
    """
    print(logo)


def print_welcome() -> None:
    """Display welcome message and instructions."""
    welcome = """
    🎉 Welcome to the PyTorch Computer Vision Template! 🎉

    This template will help you scaffold a production-ready computer vision
    project with the following features:

    ✨ Features:
      • PyTorch-based training and inference pipeline
      • Docker support (CUDA & CPU variants)
      • MLflow experiment tracking (optional)
      • UV package management
      • Pre-configured project structure
      • Development and deployment dependencies

    📋 You'll be asked the following questions:
    
    1. full_name
       → Your full name (used in project metadata and author fields)
    
    2. organization
       → Your organization/company name (used in Docker images and namespaces)
    
    3. email
       → Your email address (used for project metadata and MLflow admin)
    
    4. project_name
       → Display name for your project (can include spaces, e.g., "My CV Project")
    
    5. project_description
       → Brief description of your project (used in README and package metadata)
    
    6. python_version
       → Python version to use (e.g., "3.11", "3.12") - affects Docker and environment
    
    7. use_cuda_default
       → Use CUDA-enabled Docker base image? (y/n)
       → Choose 'n' if you're on Apple Silicon or don't need GPU support
    
    8. cuda_version
       → CUDA version for Docker (only used if use_cuda_default is 'y')
    
    9. enable_mlflow_tracking
       → Enable MLflow experiment tracking? (y/n)
       → If 'y', creates MLflow server setup with docker-compose
    
    10. install_dependencies
        → Automatically install dependencies after generation? (y/n)
        → If 'y', runs 'uv sync --extra dev' automatically
    
    11. default_device
        → Default PyTorch device for training ("cuda", "cpu", or "mps" for Apple Silicon)
        → This is the runtime device preference, separate from Docker CUDA setting
    
    12. repo_visibility
        → Git repository visibility preference ("private" or "public")

    💡 Tips:
      • Press Enter to accept default values (shown in brackets)
      • Defaults are optimized for most use cases
      • You can always modify settings later in the generated project
      • For Apple Silicon Macs: set use_cuda_default='n' and default_device='mps'

    Let's get started! 🚀
    """
    print(welcome)


def wait_for_continue() -> None:
    """Wait for user to press Enter before continuing."""
    try:
        input("\n" + "=" * 60 + "\n" + "Press Enter to continue with project setup... ")
        print("\n")
    except (EOFError, KeyboardInterrupt):
        # Handle cases where input might not be available
        print("\n")
        sys.exit(0)


def main() -> None:
    """Main entry point for pre-generation hook."""
    try:
        print_logo()
        print_welcome()
        wait_for_continue()
    except Exception as e:
        # Don't fail the generation if logo/welcome fails
        print(f"⚠️  Warning: Could not display welcome message: {e}\n")
        sys.exit(0)  # Exit 0 to continue generation


if __name__ == "__main__":
    main()

