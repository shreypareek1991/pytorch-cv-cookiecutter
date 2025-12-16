"""Test that all imports work correctly."""

import pytest


def test_package_import() -> None:
    """Test that the main package can be imported."""
    import {{ cookiecutter.python_package }}

    assert hasattr({{ cookiecutter.python_package }}, "__version__")


def test_utils_import() -> None:
    """Test that utils can be imported."""
    from {{ cookiecutter.python_package }}.utils import load_state, save_state

    assert callable(load_state)
    assert callable(save_state)


def test_vision_import() -> None:
    """Test that vision module can be imported."""
    from {{ cookiecutter.python_package }}.vision import load_image, preprocess_image, predict_simple

    assert callable(load_image)
    assert callable(preprocess_image)
    assert callable(predict_simple)


def test_app_import() -> None:
    """Test that app can be imported."""
    import app.main

    assert hasattr(app.main, "app")
