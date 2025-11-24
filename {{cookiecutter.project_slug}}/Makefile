.PHONY: sync dev test format lint train docker-build docker-run

sync:
	uv sync --all-extras

dev:
	uv run pre-commit install

test:
	uv run pytest

format:
	uv run ruff format

lint:
	uv run ruff check
	uv run mypy src

train:
	uv run python scripts/train.py run

docker-build:
	bash docker/build.sh

docker-run:
	bash docker/run.sh

