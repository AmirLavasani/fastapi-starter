import typer

from app.version import __version__
from app.main import run_service


cli = typer.Typer()

@cli.command()
def run(host: str = "0.0.0.0", port: int = 8080):
    run_service(host, port)


@cli.command()
def version():
    print(f"🚀 {__version__} 👀")


if __name__ == "__main__":
    cli()