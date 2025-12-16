# Notebooks

This directory contains Jupyter notebooks for data exploration, experimentation, and analysis.

## Usage

Notebooks in this directory are excluded from pre-commit hooks (except for black formatting which is helpful).

You can format notebooks using:

```bash
# Format all Python files including notebooks
make format
```

## Structure

- `exploration/` - Data exploration notebooks
  - `01_data_exploration.ipynb` - Initial data exploration and analysis
- `experiments/` - Model training and experimentation notebooks
  - `01_model_experiment.ipynb` - Model training and evaluation experiments
- `visualization/` - Results visualization notebooks
  - `01_results_visualization.ipynb` - Visualization of results and predictions

## Data Directory Structure

The `science/data/` directory is organized as follows:

- `raw/` - Original, unprocessed data (gitignored)
- `processed/` - Final, canonical data sets for modeling (gitignored)
- `external/` - Data from external sources (gitignored)
- `interim/` - Intermediate data that has been transformed (gitignored)
- `output/` - Generated outputs like figures, reports, etc. (gitignored)

All notebooks include pathing code to access:
- Data from `science/data/` subdirectories
- Models from `science/models/`
- Code from the `{{ cookiecutter.python_package }}` package

