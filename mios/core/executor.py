import subprocess
from rich import print

def install_python_package(package):

    print(f"[cyan]Installing package:[/cyan] {package}")

    try:
        subprocess.run(
            ["python", "-m", "pip", "install", package],
            check=True
        )

        print("[green]Installation complete[/green]")

    except subprocess.CalledProcessError:

        print("[red]Installation failed[/red]")

def run_action(plan):
    if plan["action"] == "install_package":
        package = plan["package"]
        print(f"[cyan]Running command:[/cyan] python -m pip install {package}")
        install_python_package(package)

