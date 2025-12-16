.PHONY: help sync dev test format lint app docker pre-commit docs

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
	@echo "API Application:"
	@echo "  make app               Run FastAPI application (development)"
	@echo "  make app serve         Run FastAPI application (development)"
	@echo ""
	@echo "Docker:"
	@echo "  make docker build      Build Docker image (auto-switches to CPU on ARM)"
	@echo "  make docker build-cpu  Build CPU-only image"
	@echo "  make docker build-cuda Build CUDA image (x86_64 Linux only)"
	@echo "  make docker build-scan Build and scan Docker image"
	@echo "  make docker run        Run Docker container"
	@echo "  make docker scan       Scan existing Docker image"
	@echo ""
	@echo "Documentation:"
	@echo "  make docs              Serve documentation website (default)"
	@echo "  make docs serve        Serve documentation website"
	@echo "  make docs build        Build static documentation site"
	@echo ""
	@echo "For more information, see README.md or docs/"

sync: ## Sync all dependencies
	uv sync --all-extras

dev: pre-commit-install ## Install pre-commit hooks

test: ## Run tests
	uv run pytest

format: ## Format code (black, isort, ruff)
	uv run black {{ cookiecutter.python_package }} app tests science
	uv run isort {{ cookiecutter.python_package }} app tests
	uv run ruff format {{ cookiecutter.python_package }} app tests

lint: ## Lint code (ruff, mypy)
	uv run ruff check {{ cookiecutter.python_package }} app tests
	uv run mypy {{ cookiecutter.python_package }} app

app: app-serve ## Run FastAPI application (development)

app-serve: ## Run FastAPI application (development)
	uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8080

docker: ## Docker commands (use: make docker build, make docker run, etc.)
	@echo "Available docker commands:"
	@echo "  make docker build      Build Docker image"
	@echo "  make docker build-cpu  Build CPU-only image"
	@echo "  make docker build-cuda Build CUDA image"
	@echo "  make docker build-scan Build and scan Docker image"
	@echo "  make docker run        Run Docker container"
	@echo "  make docker scan       Scan existing Docker image"

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

docs: docs-serve ## Serve documentation website (default)

docs-serve: ## Serve documentation website
	uv run mkdocs serve

docs-build: ## Build static documentation site
	uv run mkdocs build

