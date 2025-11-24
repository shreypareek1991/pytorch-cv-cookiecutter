import importlib


def test_project_imports() -> None:
    assert importlib.import_module("{{ cookiecutter.python_package }}") is not None

