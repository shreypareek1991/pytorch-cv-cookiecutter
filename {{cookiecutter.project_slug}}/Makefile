.PHONY: sync dev test format lint train docker-build docker-run pre-commit docs docs-serve docs-build

sync:
	uv sync --all-extras

dev: pre-commit-install

test:
	uv run pytest

format:
	uv run black src scripts tests
	uv run isort src scripts tests
	uv run ruff format

lint:
	uv run ruff check
	uv run mypy src

train:
	uv run python scripts/train.py run

docker-build:
	bash docker/build.sh

docker-build-cpu:
	bash docker/build.sh --cpu

docker-build-cuda:
	bash docker/build.sh

docker-build-scan:
	bash docker/build.sh --scan

docker-run:
	bash docker/run.sh

docker-scan:
	bash docker/scan.sh

pre-commit:
	uv run pre-commit run --all-files

pre-commit-install:
	uv run pre-commit install

docs:
	uv run mkdocs serve

docs-serve:
	uv run mkdocs serve

docs-build:
	uv run mkdocs build

