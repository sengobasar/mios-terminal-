import typer
from rich import print
from mios.debug.error_parser import parse_error

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


@app.command()
def doctor():
    """
    Show system health
    """
    print("[cyan]System diagnostic coming soon...[/cyan]")


def main():
    app()


if __name__ == "__main__":
    main()