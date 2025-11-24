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

    📋 You'll be asked a few questions to customize your project:
      • Your name and organization
      • Project details (name, description)
      • Python version
      • Docker configuration (CUDA support)
      • MLflow tracking preferences
      • Git repository settings

    💡 Tips:
      • Press Enter to accept default values (shown in brackets)
      • Defaults are optimized for most use cases
      • You can always modify settings later

    Let's get started! 🚀
    """
    print(welcome)


def main() -> None:
    """Main entry point for pre-generation hook."""
    try:
        print_logo()
        print_welcome()
        print("\n" + "=" * 60 + "\n")
    except Exception as e:
        # Don't fail the generation if logo/welcome fails
        print(f"⚠️  Warning: Could not display welcome message: {e}\n")
        sys.exit(0)  # Exit 0 to continue generation


if __name__ == "__main__":
    main()

