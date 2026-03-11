import typer
from rich import print
from mios.tools.system_info import get_system_info
import json

app = typer.Typer()

@app.command()
def debug():
    """
    Run error debugging pipeline
    """
    pass

@app.command()
def doctor():
    """
    Check system health
    """

    system_info = get_system_info()

    print("\n[green]System Information:[/green]")
    print(json.dumps(system_info, indent=4))

def main():
    app()

if __name__ == "__main__":
    main()
