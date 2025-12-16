"""{{ cookiecutter.project_description }}."""

from importlib import metadata as _metadata

__all__ = ["__version__"]

try:
    __version__ = _metadata.version("{{ cookiecutter.project_slug }}")
except _metadata.PackageNotFoundError:  # pragma: no cover - during local dev
    __version__ = "0.0.0"
