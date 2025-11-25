.PHONY: help sync dev test format lint train docker-build docker-run pre-commit docs docs-serve docs-build

.DEFAULT_GOAL := help

help: ## Show this help message
	@echo "Available commands:"
	@echo ""
	@echo "Environment Management:"
	@echo "  make sync              Sync all dependencies (uv sync --all-extras)"
	@echo "  make dev               Install pre-commit hooks"
	@echo ""
	@echo "Code Quality:"
	@echo "  make format            Format code (black, isort, ruff)"
	@echo "  make lint              Lint code (ruff, mypy)"
	@echo "  make test              Run tests (pytest)"
	@echo "  make pre-commit        Run all pre-commit checks manually"
	@echo ""
	@echo "Training:"
	@echo "  make train             Run training script"
	@echo ""
	@echo "Docker:"
	@echo "  make docker-build      Build Docker image (auto-switches to CPU on ARM)"
	@echo "  make docker-build-cpu  Build CPU-only image"
	@echo "  make docker-build-cuda Build CUDA image (x86_64 Linux only)"
	@echo "  make docker-build-scan Build and scan Docker image"
	@echo "  make docker-run        Run Docker container"
	@echo "  make docker-scan       Scan existing Docker image"
	@echo ""
	@echo "Documentation:"
	@echo "  make docs              Serve documentation website (default)"
	@echo "  make docs-serve        Serve documentation website"
	@echo "  make docs-build        Build static documentation site"
	@echo ""
	@echo "For more information, see README.md or docs/"

sync: ## Sync all dependencies
	uv sync --all-extras

dev: pre-commit-install ## Install pre-commit hooks

test: ## Run tests
	uv run pytest

format: ## Format code (black, isort, ruff)
	uv run black src scripts tests
	uv run isort src scripts tests
	uv run ruff format

lint: ## Lint code (ruff, mypy)
	uv run ruff check
	uv run mypy src

train: ## Run training script
	uv run python scripts/train.py run

docker-build: ## Build Docker image (auto-switches to CPU on ARM)
	bash docker/build.sh

docker-build-cpu: ## Build CPU-only image
	bash docker/build.sh --cpu

docker-build-cuda: ## Build CUDA image (x86_64 Linux only)
	bash docker/build.sh

docker-build-scan: ## Build and scan Docker image
	bash docker/build.sh --scan

docker-run: ## Run Docker container
	bash docker/run.sh

docker-scan: ## Scan existing Docker image
	bash docker/scan.sh

pre-commit: ## Run all pre-commit checks manually
	uv run pre-commit run --all-files

pre-commit-install: ## Install pre-commit hooks
	uv run pre-commit install

docs: ## Serve documentation website (default)
	uv run mkdocs serve

docs-serve: ## Serve documentation website
	uv run mkdocs serve

docs-build: ## Build static documentation site
	uv run mkdocs build

