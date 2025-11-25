#!/bin/bash
# Wrapper script to show welcome message before cookiecutter prompts

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
HOOKS_DIR="$SCRIPT_DIR/hooks"

# Display logo
if [ -f "$HOOKS_DIR/logo.txt" ]; then
    cat "$HOOKS_DIR/logo.txt"
else
    echo "Logo file not found"
fi

# Display welcome message
cat << 'EOF'

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

EOF

echo ""
echo "============================================================"
read -p "Press Enter to continue with project setup... "
echo ""
echo ""

# Now run cookiecutter
if [ "$#" -eq 0 ]; then
    # If no arguments, use the GitHub URL
    cookiecutter https://github.com/shreypareek1991/pytorch-cv-cookiecutter
else
    # Pass through any arguments
    cookiecutter "$@"
fi


