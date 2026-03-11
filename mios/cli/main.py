import typer
from rich import print
from mios.debug.error_parser import parse_error
from mios.core.planner import plan_from_error
from mios.core.executor import run_action

app = typer.Typer()

@app.command()
def debug():
    """
    Debug terminal errors
    """

    print("[yellow]Paste your error below:[/yellow]")
    error = input("> ")

    analysis = parse_error(error)

    print("\n[green]Analysis:[/green]")
    print(analysis)

    plan = plan_from_error(error)

    print("\n[green]Action Plan:[/green]")
    print(plan)

    if typer.confirm("Run action?"):
        run_action(plan)

def main():
    app()

if __name__ == "__main__":
    main()
