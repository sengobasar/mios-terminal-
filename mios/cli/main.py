import typer
import re
import json
from pathlib import Path
from typing import Optional
from rich import print
from rich.prompt import Prompt

from mios.tools.system_info import get_system_info
from mios.core.session import Session
from mios.debug.error_parser import parse_error
from mios.core.planner import plan_from_error
from mios.core.executor import run_action

from mios.core.interpreter import interpret_intent
from mios.ai.intent_classifier import classify_intent
from mios.ai.command_llm import interpret_with_llm
from mios.core.agent_loop import run_agent

app = typer.Typer()


# =========================
# INTERACTIVE SHELL
# =========================

def interactive_shell(project_path: Optional[str] = None):
    """Start interactive MIOS shell with optional project context."""
    session = Session()

    if project_path:
        session.scan_project(project_path)

    print("\n[bold green]MIOS Interactive Shell[/bold green]")

    if session.project_files:
        print(f"[dim]Project: {project_path}[/dim]")

    print("Type 'exit' to quit\n")

    while True:

        prompt = f"mios ({session.current_file or 'no file'})>" if session.current_file else "mios>"
        user_input = Prompt.ask(prompt)

        if user_input.lower() in ("exit", "quit"):
            break

        try:

            # Explicit run command
            match = re.search(r"^run\s+([\w\-]+\.py)$", user_input.strip())

            if match:
                file_name = match.group(1)
                print(f"[cyan]Running agent on Python file: {file_name}[/cyan]")
                run_agent(file_name)
                continue

            intent_data = classify_intent(user_input)

            # LLM fallback
            if intent_data["intent"] == "unknown":

                print("[yellow]Using LLM interpreter...[/yellow]")

                action = interpret_with_llm(user_input)

                if action["action"] == "create_file":

                    with open(action["file"], "w", encoding="utf-8") as f:
                        f.write(action.get("content", ""))

                    print(f"[green]File created:[/green] {action['file']}")

                elif action["action"] == "install_package":

                    import subprocess
                    subprocess.run(["pip", "install", action["package"]])

                    print(f"[green]Package installed:[/green] {action['package']}")

                elif action["action"] == "run_command":

                    import subprocess
                    subprocess.run(action["command"], shell=True)

                    print(f"[green]Command executed:[/green] {action['command']}")

                continue

            action = interpret_intent(intent_data["intent"], user_input)

            if "command" in action or "action" in action:

                print(f"[blue]Executing: {action.get('command', action.get('action'))}[/blue]")
                run_action(action)

            else:

                print(f"[cyan]Agent response: {action}[/cyan]")

        except Exception as e:
            print(f"[red]Error: {str(e)}[/red]")


# =========================
# COMMANDS
# =========================

@app.command()
def mios(project: Optional[str] = typer.Argument(None)):
    """Start MIOS interactive shell."""
    interactive_shell(project_path=project)


@app.command()
def debug():
    """Run error debugging pipeline."""

    error = input("Paste the error: ")

    analysis = parse_error(error)

    print(f"\n[yellow]Analysis:[/yellow]\n{json.dumps(analysis, indent=4)}")

    plan = plan_from_error(error)

    print(f"\n[yellow]Action Plan:[/yellow]\n{json.dumps(plan, indent=4)}")

    confirmation = input("Confirm to run the action plan? (y/n): ")

    if confirmation.lower() == "y":

        if plan["action"] != "none":
            run_action(plan)


@app.command()
def doctor():
    """Check system health."""

    system_info = get_system_info()

    print("\n[green]System Information:[/green]")
    print(json.dumps(system_info, indent=4))


@app.command()
def run():
    """Run a command based on intent."""

    user_input = input("Enter your command or intent: ")

    intent_data = classify_intent(user_input)
    intent = intent_data["intent"]

    if intent == "unknown":
        print("\n[red]Error:[/red] Unknown intent")
        return

    action = interpret_intent(intent, user_input)

    if "command" in action:

        print(f"\n[yellow]Command to be executed:[/yellow]\n{action['command']}")

        confirmation = input("Confirm to run the command? (y/n): ")

        if confirmation.lower() == "y":
            run_action(action)

    elif "action" in action:

        print(f"\n[yellow]Action to be executed:[/yellow]\n{action['action']}")

        confirmation = input("Confirm to run the action? (y/n): ")

        if confirmation.lower() == "y":
            run_action(action)

    else:

        print("\n[red]Error:[/red] Unknown action")


@app.command()
def edit(file_path: str):
    """Open a file for editing with MIOS."""

    session = Session()
    session.update_file_context(file_path)

    print(f"[green]Editing:[/green] {file_path}")

    content = Path(file_path).read_text()

    print(f"\nFile content:\n{content}")


@app.command()
def new(file_path: str):
    """Create a new file."""

    Path(file_path).touch()

    print(f"[green]Created:[/green] {file_path}")

    edit(file_path)


@app.command()
def project(init_path: str = "."):
    """Initialize a MIOS project."""

    session = Session()
    session.scan_project(init_path)

    print(f"[green]Project initialized:[/green] {init_path}")
    print(f"Found {len(session.project_files)} files")


# =========================
# ENTRY POINT
# =========================

def main():
    app()


if __name__ == "__main__":
    main()