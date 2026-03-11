import subprocess
from rich import print


def install_python_package(package):

    print(f"[cyan]Installing package:[/cyan] {package}")

    try:
        subprocess.run(
            ["pip", "install", package],
            check=True
        )

        print("[green]Installation complete[/green]")

    except subprocess.CalledProcessError:

        print("[red]Installation failed[/red]")