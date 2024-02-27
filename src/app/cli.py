import typer
from colorama import Fore, Back, Style

from app.version import __version__, __template_version__
from app.main import run_service


cli = typer.Typer()

version_colored = Fore.CYAN + Style.BRIGHT + "v" + __version__ + Style.RESET_ALL
template_version_colored = Fore.RED + Style.BRIGHT + "v" + __template_version__ + Style.RESET_ALL

@cli.command()
def run(host: str = "0.0.0.0", port: int = 8080):
    print(f"Running service {version_colored} 🚀 via fastapi-starter template {template_version_colored} 📦")
    run_service(host, port)


@cli.command()
def version():
    print(f"🚀 {__version__}")


if __name__ == "__main__":
    cli()
