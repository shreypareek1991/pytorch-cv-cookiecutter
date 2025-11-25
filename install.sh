#!/bin/bash
# One-liner installer that shows welcome message before running cookiecutter
# Usage: curl -fsSL https://raw.githubusercontent.com/shreypareek1991/pytorch-cv-cookiecutter/main/install.sh | bash

set -e

REPO_URL="https://github.com/shreypareek1991/pytorch-cv-cookiecutter"
TEMP_DIR=$(mktemp -d)

# Cleanup on exit
trap "rm -rf $TEMP_DIR" EXIT

echo "📦 Downloading template..."
git clone --depth 1 "$REPO_URL" "$TEMP_DIR" > /dev/null 2>&1

# Run the wrapper script
cd "$TEMP_DIR"
exec ./run_template.sh

