import typer
from rich import print
from mios.tools.system_info import get_system_info
import json
from mios.debug.error_parser import parse_error, plan_from_error
from mios.core.executor import run_action

app = typer.Typer()

@app.command()
def debug():
    """
    Run error debugging pipeline
    """

    error = input("Paste the error: ")
    analysis = parse_error(error)
    print(f"\n[yellow]Analysis:[/yellow]\n{json.dumps(analysis, indent=4)}")
    print(f"\n[yellow]Action Plan:[/yellow]\n{json.dumps(plan_from_error(error), indent=4)}")
    confirmation = input("Confirm to run the action plan? (y/n): ")
    if confirmation.lower() == "y":
        plan = plan_from_error(error)
        if plan["action"] != "none":
            run_action(plan)

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
