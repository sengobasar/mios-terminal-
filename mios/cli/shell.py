import json
from rich import print
from mios.core.agent_loop import run_agent

def interactive_shell():
    """
    Implements an interactive shell for MIOS, allowing users to input problems
    and observe the agent's reasoning process and results.
    """
    print("[bold green]Welcome to MIOS Interactive Shell![/bold green]")
    print("[yellow]Type your problem, or 'exit' to quit.[/yellow]")

    while True:
        try:
            user_input = input("[bold blue]MIOS > [/bold blue]")

            if user_input.lower().strip() == "exit":
                print("[green]Exiting MIOS Shell. Goodbye![/green]")
                break
            
            if not user_input.strip():
                print("[yellow]Please enter a problem or 'exit' to quit.[/yellow]")
                continue

            print(f"[bold magenta]Agent working on:[/bold magenta] {user_input}")
            final_state = run_agent(user_input)
            
            print("\n[bold green]Agent Run Complete. Final State:[/bold green]")
            print(json.dumps(final_state, indent=4))

        except KeyboardInterrupt:
            print("\n[yellow]Interrupted by user. Type 'exit' to quit, or continue.[/yellow]")
        except Exception as e:
            print(f"[red]An unexpected error occurred: {e}[/red]")
            # Optionally, you could call run_agent with the error to debug itself
            # run_agent(f"Debug this error: {e}")
