import typer
import re
from rich import print
from rich.prompt import Prompt
from mios.tools.system_info import get_system_info
import json

from mios.debug.error_parser import parse_error
from mios.core.planner import plan_from_error
from mios.core.executor import run_action

from mios.core.interpreter import interpret_intent
from mios.ai.intent_classifier import classify_intent
from mios.core.agent_loop import run_agent

app = typer.Typer()

def interactive_shell():
    """Start interactive MIOS shell."""
    print("\n[bold green]MIOS Interactive Shell[/bold green]")
    print("Type 'exit' to quit\n")
    
    while True:
        user_input = Prompt.ask("mios>")
        
        if user_input.lower() in ('exit', 'quit'):
            break
            
        try:
            # First try to detect and run Python files in command
            match = re.search(r"([\w\-]+\.py)", user_input)
            if match:
                file_name = match.group(1)
                print(f"[cyan]Running agent on Python file: {file_name}[/cyan]")
                run_agent(file_name)
                continue
                
            intent_data = classify_intent(user_input)
            
            if intent_data["intent"] == "unknown":
                print(f"[yellow]Unable to determine intent for: {user_input}[/yellow]")
                continue
                
            action = interpret_intent(intent_data["intent"], user_input)
            
            if "command" in action or "action" in action:
                print(f"[blue]Executing: {action.get('command', action.get('action'))}[/blue]")
                run_action(action)
            else:
                print(f"[cyan]Agent response: {action}[/cyan]")
                
        except Exception as e:
            print(f"[red]Error: {str(e)}[/red]")


@app.command()
def mios():
    """Start MIOS interactive shell."""
    interactive_shell()

@app.command()
def debug():
    """
    Run error debugging pipeline
    """

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
    """
    Check system health
    """

    system_info = get_system_info()

    print("\n[green]System Information:[/green]")
    print(json.dumps(system_info, indent=4))


@app.command()
def run():
    """
    Run a command based on user intent
    """

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


def main():
    app()


if __name__ == "__main__":
    main()
