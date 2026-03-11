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

    elif plan["action"] == "suggest_install_command":
        command = plan["command"]
        print(f"[yellow]You may need to install the command:[/yellow] {command}")

    elif plan["action"] == "suggest_run_with_sudo":
        print("[yellow]Try running the command with sudo.[/yellow]")

    elif plan["action"] == "suggest_check_file_path":
        file = plan["file"]
        print(f"[yellow]Check if the file exists:[/yellow] {file}")

