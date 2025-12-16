# DVC (Data Version Control)

This guide covers using DVC for data versioning in your project.

{% if cookiecutter.enable_dvc == "y" or cookiecutter.enable_dvc == "yes" %}
## Setup

DVC has been initialized in your project. You can start tracking data immediately.

### Initial Configuration

```bash
# Check DVC status
dvc status

# Configure remote storage (optional but recommended)
# Example for S3 (requires dvc-s3):
# First install: uv add dvc-s3
# Then configure:
# dvc remote add -d myremote s3://my-bucket/dvc-storage

# Or for local storage:
dvc remote add -d myremote /path/to/storage

# Or for other cloud storage, install the appropriate plugin:
# - S3: uv add dvc-s3
# - GCS: uv add dvc-gs
# - Azure: uv add dvc-azure
```

## Basic Usage

### Tracking Data

```bash
# Track raw data
dvc add science/data/raw/

# Track processed data
dvc add science/data/processed/

# Track models
dvc add science/models/
```

### Committing Changes

```bash
# After adding data with DVC
git add science/data/raw.dvc science/data/raw.dvc
git commit -m "Add raw dataset v1.0"
git push

# Push data to remote storage
dvc push
```

### Retrieving Data

```bash
# Pull data from remote storage
dvc pull

# Checkout specific version
dvc checkout science/data/raw.dvc
```

## Workflow

1. **Add new data version:**
   ```bash
   dvc add science/data/raw/
   git add science/data/raw.dvc .gitignore
   git commit -m "Update raw data to v2.0"
   dvc push
   git push
   ```

2. **Switch between versions:**
   ```bash
   git checkout <commit-hash>
   dvc checkout
   ```

3. **Compare data versions:**
   ```bash
   dvc diff science/data/raw.dvc
   ```

## Configuration

DVC configuration is stored in `.dvc/config`. You can edit it directly or use commands:

```bash
# List remotes
dvc remote list

# Modify remote
dvc remote modify myremote url s3://new-bucket/path

# Remove remote
dvc remote remove myremote
```

## Best Practices

1. **Track large files**: Use DVC for files > 100MB
2. **Commit .dvc files**: Always commit `.dvc` files to git
3. **Use remote storage**: Store data in cloud storage (S3, GCS, Azure)
4. **Tag versions**: Use git tags for important data versions
5. **Document changes**: Add notes in commit messages about data changes

## Integration with Notebooks

In your notebooks, you can use DVC to ensure you're using the correct data version:

```python
import subprocess
from pathlib import Path

# Ensure you have the latest data
subprocess.run(["dvc", "pull"], check=True)

# Or checkout specific version
# subprocess.run(["dvc", "checkout", "science/data/raw.dvc"], check=True)
```

## Troubleshooting

**Issue**: `dvc: command not found`
- **Solution**: Install DVC with `uv sync --extra dvc` or `pip install dvc`

**Issue**: Remote storage not configured
- **Solution**: Configure with `dvc remote add -d myremote <storage-url>`

**Issue**: Data not syncing
- **Solution**: Run `dvc pull` to fetch data from remote storage

For more information, see the [DVC documentation](https://dvc.org/doc).
{% else %}
DVC is not enabled in this project. To enable it:

1. Re-run cookiecutter and select "yes" for DVC
2. Or manually install: `uv sync --extra dvc`
3. Initialize: `dvc init`
4. Configure remote storage: `dvc remote add -d myremote <storage-url>`

For more information, see the [DVC documentation](https://dvc.org/doc).
{% endif %}

