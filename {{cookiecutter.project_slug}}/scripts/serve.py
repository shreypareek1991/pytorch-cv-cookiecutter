from __future__ import annotations

import typer
import uvicorn

app = typer.Typer(help="Serve the FastAPI inference app.")


@app.command()
def api(host: str = "0.0.0.0", port: int = 8000, workers: int = 1) -> None:
    uvicorn.run(
        "{{ cookiecutter.python_package }}.deployment.service:app",
        host=host,
        port=port,
        workers=workers,
    )


if __name__ == "__main__":
    app()

